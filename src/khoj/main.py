""" Main module for Khoj Assistant
   isort:skip_file
"""

# Standard Packages
from contextlib import redirect_stdout
import io
import os
import sys
import locale

from dotenv import load_dotenv
import logging
import threading
import warnings
from importlib.metadata import version

from khoj.utils.helpers import in_debug_mode

# Ignore non-actionable warnings
warnings.filterwarnings(
    "ignore", 
    message=r"snapshot_download.py has been made private", 
    category=FutureWarning)
warnings.filterwarnings(
    "ignore", 
    message=r"legacy way to download files from the HF hub,", 
    category=FutureWarning)

import uvicorn
import django
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import schedule

from django.core.asgi import get_asgi_application
from django.core.management import call_command

load_envvars = load_dotenv(
    f".envs/{os.getenv('ENV_VERSION', 'default')}")
assert load_envvars, f"Did not load env vars from .envs/{os.getenv('ENV_VERSION', 'default')}"
# Initialize Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "khoj.app.settings")
django.setup()

# Initialize Django Database
db_migrate_output = io.StringIO()
with redirect_stdout(db_migrate_output):
    call_command("migrate", "--noinput")

# Initialize Django Static Files
collectstatic_output = io.StringIO()
with redirect_stdout(collectstatic_output):
    call_command("collectstatic", "--noinput")

# Initialize the Application Server
if in_debug_mode():
    app = FastAPI(debug=True, docs_url="/docs")
else:
    # app = FastAPI(docs_url=None)  # Disable Swagger UI in production
    app = FastAPI(docs_url="/docs")  

# Get Django Application
django_app = get_asgi_application()

# Add CORS middleware
KHOJ_DOMAIN = os.getenv("KHOJ_DOMAIN", "app.khoj.dev")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "app://obsidian.md",
        "capacitor://localhost",  # To allow access from Obsidian iOS app using Capacitor.JS
        "http://localhost",  # To allow access from Obsidian Android app
        "http://localhost:*",
        "http://127.0.0.1:*",
        f"https://{KHOJ_DOMAIN}",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set Locale
locale.setlocale(locale.LC_ALL, "")

# Internal Packages. We do this after setting up Django so that Django features are accessible to the app.
from khoj.configure import configure_routes, initialize_server, configure_middleware
from khoj.utils import state
from khoj.utils.cli import cli
from khoj.utils.initialization import initialization

# Setup Logger
from khoj.log_configs import logger

# logger = logging.getLogger("khoj")

def run(should_start_server=True):
    """
    A function that runs the main logic of the program. It initializes various settings, logs initialization steps, creates necessary directories, sets up logging, starts the server, configures routes, mounts necessary directories, configures middleware, and finally starts the server based on the provided arguments.
    Parameters:
    - should_start_server: a boolean indicating whether the server should be started.
    """
    # Turn Tokenizers Parallelism Off. App does not support it.
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    # Load config from CLI
    state.cli_args = sys.argv[1:]
    args = cli(state.cli_args)
    set_state(args)

    # Set Logging Level
    if args.verbose == 0:
        logger.setLevel(logging.INFO)
    elif args.verbose >= 1:
        logger.setLevel(logging.DEBUG)

    logger.info(f"🚒 Initializing Khoj v{state.khoj_version}")
    logger.info(f"📦 Initializing DB:\n{db_migrate_output.getvalue().strip()}")
    logger.debug(f"🌍 Initializing Web Client:\n{collectstatic_output.getvalue().strip()}")
    # initialize Chat configuration based on the `ChatModelObject`
    """
    class ChatModelOptions(BaseModel):
    class ModelType(models.TextChoices):
        OPENAI = "openai"
        OFFLINE = "offline"

    max_prompt_size = models.IntegerField(default=None, null=True, blank=True)
    tokenizer = models.CharField(max_length=200, default=None, null=True, blank=True)
    chat_model = models.CharField(max_length=200, default="mistral-7b-instruct-v0.1.Q4_0.gguf")
    model_type = models.CharField(max_length=200, choices=ModelType.choices, default=ModelType.OFFLINE)
    """
    initialization()

    # Create app directory, if it doesn't exist
    state.config_file.parent.mkdir(parents=True, exist_ok=True)

    # Set Log File
    fh = logging.FileHandler(state.config_file.parent / "khoj.log", encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    logger.info("🌘 Starting Khoj")

    # Setup task scheduler
    poll_task_scheduler()

    # Start Server
    configure_routes(app)

    #  Mount Django and Static Files
    app.mount("/server", django_app, name="server")
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    if not os.path.exists(static_dir):
        os.mkdir(static_dir)
    app.mount(f"/static", StaticFiles(directory=static_dir), name=static_dir)

    # Configure Middleware
    configure_middleware(app)

    initialize_server(args.config)

    # If the server is started through gunicorn (external to the script), don't start the server
    if should_start_server:
        start_server(app, host=args.host, port=args.port, socket=args.socket)

# Set State for application
def set_state(args):
    state.config_file = args.config_file
    state.config = args.config
    state.verbose = args.verbose
    state.host = args.host
    state.port = args.port
    state.anonymous_mode = args.anonymous_mode
    state.khoj_version = version("khoj-assistant")
    state.chat_on_gpu = args.chat_on_gpu


def start_server(app, host=None, port=None, socket=None, reload=False):
    logger.info("🌖 Khoj is ready to use")
    if socket:
        uvicorn.run(app, proxy_headers=True, uds=socket, log_level="debug", use_colors=True, log_config=None, reload=reload)
    else:
        uvicorn.run(app, host=host, port=port, log_level="debug", use_colors=True, log_config=None, reload=reload)
    logger.info("🌒 Stopping Khoj")


def poll_task_scheduler():
    timer_thread = threading.Timer(60.0, poll_task_scheduler)
    timer_thread.daemon = True
    timer_thread.start()
    schedule.run_pending()


if __name__ == "__main__":
    run()
else:
    run(should_start_server=False)
