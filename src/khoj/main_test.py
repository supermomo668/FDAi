from fastapi import FastAPI, HTTPException, Request, Response, Depends, Header
from fastapi.responses import JSONResponse

from fastapi.responses import StreamingResponse

from typing import Optional, Annotated
import json

import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename=f"debug_{datetime.now().strftime('%Y%m%d_%H')}.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

from pydantic  import BaseModel, Field
from typing import List, Optional, ByteString

class Message(BaseModel):
    role: str
    text: str


class ChatRequest(BaseModel):
    # messages: list[Message] = Field(..., example=[{"role": "user", "text": "Hi"}])
    body: Optional[str | List]


class ChatParameters(BaseModel):
    message: Optional[dict] = {}
    q: Optional[str] = None
    n : Optional[int] = 5
    d : Optional[float] = 0.18
    stream : Optional[bool] = False
    slug: Optional[str] = None
    conversation_id: Optional[int] = None
    city: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None

class SearchParameters(BaseModel):
    q: Optional[str] = None
    n: Optional[int] = 5
    t: Optional[str] = 'all'
    r: Optional[bool] = False
    max_distance: Optional[float] = None
    dedupe: Optional[bool] = True
    
class CommonQueryParamsClass:
    def __init__(
        self,
        client: Optional[str] = None,
        user_agent: Optional[str] = Header(None),
        referer: Optional[str] = Header(None),
        host: Optional[str] = Header(None),
    ):
        self.client = client
        self.user_agent = user_agent
        self.referer = referer
        self.host = host

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "app://obsidian.md",
        "capacitor://localhost",  # To allow access from Obsidian iOS app using Capacitor.JS
        "http://localhost",  # To allow access from Obsidian Android app
        "http://localhost:*",
        "http://127.0.0.1:*",
        "app://khoj.dev",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CommonQueryParams = Annotated[CommonQueryParamsClass, Depends()]

# Stub for the chat function
@app.get("/api/chat", response_class=Response)
async def chat(
    request: Request,
    common: CommonQueryParams,
    chat_params: ChatParameters = Depends(ChatParameters)) -> Response:
    logging.debug(f"Chat function called with params{chat_params.model_dump()}")
    print("request:", await request.json())
    print("common:", common)
    print("q:", chat_params)
    response_dict = {
        "response": "The FDAi Act project is a comprehensive initiative that aims to revolutionize healthcare through the integration of AI and data analysis. The project is divided into several key sections:\n\n1. **AI-Driven Personal Health Management**: This section focuses on leveraging AI to improve personal health outcomes. It includes the development and deployment of an AI agent designed to assist individuals and physicians.\n\n2. **Democratizing Clinical Research**: This part of the project aims to make clinical research more accessible and inclusive. It involves facilitating access to experimental therapies and minimizing related bureaucratic and financial barriers.\n\n3. **Responsibilities of the FDA**: This section details the role of the FDA in this initiative. It outlines the FDA's responsibilities in facilitating these advancements and addressing the challenges that come with them.\n\n4. **Addressing Bureaucratic, Ethical, and Data Management Challenges**: This section of the project focuses on the potential challenges that may arise from the integration of AI in healthcare. It includes strategies for managing data, addressing ethical concerns, and navigating bureaucratic hurdles.\n\n5. **Legislative Framework**: This part of the project involves the creation of a robust legislative framework that supports the integration of AI in healthcare, ensuring a transformative impact on the sector.\n\nThese sections together form the backbone of the FDAi Act project, each playing a crucial role in achieving the project's overall objective of improving health outcomes through the innovative use of AI and data analysis.",
        "context": [
            "Commit message from FDA-AI/FDAi:\nFDAi Act objectives\n\nThis commit introduces the new objectives documentation for the FDAi Act, detailing the critical role of AI and data analysis for improving health outcomes and decision-making. It further details the responsibilities of the FDA in facilitating access to experimental therapies and minimizing related bureaucratic and financial barriers. Additionally, the document outlines plans for the development and deployment of an AI agent designed to assist individuals and physicians.",
            "Commit message from FDA-AI/FDAi:\nFDAi Act objectives\n\nThis commit introduces the new objectives documentation for the FDAi Act, detailing the critical role of AI and data analysis for improving health outcomes and decision-making. It further details the responsibilities of the FDA in facilitating access to experimental therapies and minimizing related bureaucratic and financial barriers. Additionally, the document outlines plans for the development and deployment of an AI agent designed to assist individuals and physicians.",
            "# README\n## FDAi Act\n\n\nGiven the comprehensive scope and detailed requirements provided, the FDAi Act must encapsulate a wide array of facets from AI-driven personal health management to democratizing clinical research. This extended version aims to incorporate the necessary elements into a robust legislative framework, ensuring a transformative impact on healthcare through the integration of AI, while addressing bureaucratic, ethical, and data management challenges.\n\n---",
            "# README\n## FDAi Act\n\n\nGiven the comprehensive scope and detailed requirements provided, the FDAi Act must encapsulate a wide array of facets from AI-driven personal health management to democratizing clinical research. This extended version aims to incorporate the necessary elements into a robust legislative framework, ensuring a transformative impact on healthcare through the integration of AI, while addressing bureaucratic, ethical, and data management challenges.\n\n---",
            "# project_proposal\n### Abstract\nA brief summary of the project, including its purpose and expected impact on the FDAi initiative."
        ]
    }
    return Response(
        content=json.dumps(response_dict), media_type="application/json")

def to_snake_case_from_dash(item: str):
    return item.replace("_", "-")


class ConfigBase(BaseModel):
    class Config:
        alias_generator = to_snake_case_from_dash
        populate_by_name = True

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

class SearchResponse(ConfigBase):
    entry: str
    score: float
    cross_score: Optional[float] = None
    additional: Optional[dict] = None
    corpus_id: str
    
# Stub for the search function
@app.get("/api/search")
async def search(
    request: Request,
    common: CommonQueryParams,
    search_params: SearchParameters = Depends(),
):
    print("Search:")
    # Assuming you are reading JSON body in a GET request for demonstration; typically, GET requests do not have a body.
    # It's more common to use query parameters directly or path parameters for GET requests.
    print("request:", await request.json())  # Note: GET requests typically don't include a body
    print("common:", common)
    print("q:", search_params)
    logging.debug(f"Search function called with search_params")
    
    res_dict = [
        {
            "entry": "# FDAi Platform",
            "score": 0.053477462918908,
            "cross-score": None,
            "additional": {
                "source": "github",
                "file": "https://github.com/FDA-AI/FDAi/blob/main/docs/fdai-act/platform.md",
                "compiled": "# platform\n## FDAi Platform",
                "heading": "# platform\n## FDAi Platform"
            },
            "corpus-id": "09744227-6609-49d8-8d3a-3600d83bbacc"
        },
        {
            "entry": "# FDAi Platform",
            "score": 0.053477462918908,
            "cross-score": None,
            "additional": {
                "source": "github",
                "file": "https://github.com/FDA-AI/FDAi/blob/main/docs/fdai-act/platform.md",
                "compiled": "# platform\n## FDAi Platform",
                "heading": "# platform\n## FDAi Platform"
            },
            "corpus-id": "bea3c145-9dc4-4c99-9ca6-bece8030a4fe"
        }
    ]
    return res_dict

from typing import List
def format_search_text(response: List[dict]) -> str:
    formatted_entries = []
    for entry in response:
        detail = entry.get('additional', {})
        # Format the extracted information
        formatted_entries.append(
            f"Sources: [{detail.get('source', '')}]({detail.get('file', '')})")
    return "# Additional Sources:\n" + "\n".join(f"{i}. {element}" for i, element in enumerate(formatted_entries, start=1))

def format_chat_text(response):
    return response.get('response', '') + "\n# Context:\n"+\
        '\n'.join([c.replace('#','##') for c in response.get('context', [])])
        
# Placeholder for the response formatter function
def format_chat_n_search_response(chat_response: Response, search_content: str) -> str:
    logging.debug("Formatting chat and search response")
    return f"{chat_response}\n{search_content}"

import time
def response_stream(text:str|dict, step:int=3):
    i = 0
    while i < len(text):
        yield text[i:min(i+step, len(text))]
        i += step

@app.post("/api/chat/deepchat", response_class=Response)
async def deepchat(
    request: Request,
    common: CommonQueryParams,
    chat_params: ChatParameters = Depends(ChatParameters)
) -> Response:
    try:
        body = await request.json()
        print(body, common, dict(chat_params), sep='\n')
        # Extract the last message from the messages list
        last_message = body.get('messages')[-1]
        if not last_message.get('role','')=="user":
            raise HTTPException(status_code=422, detail="message must be from 'user'")
    except Exception as e:
        raise HTTPException(status_code=422, detail="Malformed request format. Ensure 'messages' field is there with > 0 messages") from e
    query_update = {'q': last_message.get('text')}
    chat_params = ChatParameters(**{**chat_params.model_dump(), **query_update})
    print(f"Chat Params: {chat_params}")
    # Chat request
    chat_response = await chat(request, common, chat_params)
    chat_content = format_chat_text(json.loads(chat_response.body.decode("utf-8")))
    # search call
    search_params = SearchParameters(**{**chat_params.model_dump(), **query_update})
    search_response: list = await search(request, common, search_params)
    search_content = format_search_text(search_response)
    # search result
    final_content = format_chat_n_search_response(chat_content, search_content)
    return Response(
        content=json.dumps({"text": final_content}),
        media_type="application/json")
    
@app.post("/")
async def dynamic_params(
    request: Request,
    common: CommonQueryParams,
    chat_params: ChatParameters = Depends()

    ) -> Response:
    try:
        # Try to access JSON body if available
        body = await request.json()
    except Exception:
        # If JSON is not available or there's an error, default to an empty dict
        body = {}
    print(body)
    # Access query parameters (if any)
    query_params = dict(request.query_params)
    print(query_params)
    print(common.__dict__)
    # Combine query parameters and JSON body to handle them together
    # Note: Query parameters will override body parameters in case of key collisions
    combined_params = {**body, **query_params, **common.__dict__}

    # You can now process these parameters as needed
    # For demonstration, we'll just return them as a JSON response
    return Response(
        content=f"Received parameters: {combined_params}", media_type="application/json")