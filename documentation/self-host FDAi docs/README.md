## Docs for Dev

### Initialization

Set-up production version quickly by specifying the following key parameters. (may set-up a docker compose file name `docker-compose.prod.yml` optionally or rename the default one to `docker-compose.dev.yml`)
* Docker compose
  
  - DEBUG=false
  - Database credential & remove local postgres
  - Ensure it is using `prod.Dockerfile`
  - Add pgbouncer for connection management
    ```
      pgbouncer:
    image: edoburu/pgbouncer
    ports:
      - "6432:6432" # PgBouncer listening port
    env_file: .pgbouncer.env
    environment:
      # PgBouncer settings, adjust according to your needs
      POOL_MODE: session
      MAX_CLIENT_CONN: 60
      DEFAULT_POOL_SIZE: 200
    ```
    60 conn/200 pool size assuming it is Supabase PostgreSQL service
    - Ensure it lives on the same network as khoj-server `server` by specifying:
    ```
    networks:
      - default
    ```
* Django Application
  - Connect to pgbouncer by changing `POSTGRES_HOST` in `.env` to `pgbouncer` (<b>matching docker compose service name</b>)
  - Environment variables
  
* After starting the application
  - Set-up the following conversation object in `Chat Options` field in admin dashboard `server/admin`.
  
    Assuming using `gpt-4`
    ```
    max prompt size: 7000
    tokenizer: <leave blank>
    Chat model: gpt-4
    ```
    The reference to these can be found in Khoj:
    
    * default constants: `khoj/src/khoj/processor/conversation/utils.py`
    * online models: `khoj/src/khoj/processor/conversation/openai`
    
* Google Authentication <production>
  - Ensure <b> both source & redirect URL </b> is set.
    * source should be the base url
    * redirect should include `/auth/redirect/` and `/auth`
  
## Important: Development
* Data & Chat Customization
  - Chat repsonse format: 
      - require code change in `extract_references_and_questions` located in `routers/api.py`, at close to return statement
  - Data Entry
      - In `search_type/constants.py` you may modify which user is used for entry retrievers. It could be the user-self or a fixed index user
  
  
# Environment Test Sequence

* dev
  * Ensure dev DB is working
* test.pgbounceer
  * Ensure pgbouncer works with dev dev DB
* test.db
  * Ensure Prod DB is working
* test
  * Ensure Prod DB with PBBouncer is working
  
* Prod
  * deploy with gunicorn `prod.Dockerfile`
