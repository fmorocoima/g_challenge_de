import uvicorn
import argparse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from g_challenge_de.src.v1.application_api import router as application_apis
from g_challenge_de.src.core.db.create_schemas import create_all_schemas
from g_challenge_de.src.settings import (
    ENVIRONMENT, HOST, PORT
)


parser = argparse.ArgumentParser()
parser.add_argument('--createschemas', type=bool, required=False)

description = f'''<a href="https://github.com/fmorocoima/g_challenge_de">
    <img width=10% src="https://raw.githubusercontent.com/fmorocoima/g_challenge_de/develop/g_challenge_de/src/docs/assets/logo.jpg"/> Follow...</a>'''

app = FastAPI(
    title="G-challenge data engineering API serv ic e docs page", 
    description=description, 
    ) 

origins = ["*"] 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(application_apis)


if __name__ == "__main__":
    args = parser.parse_args()
    print(args.createschemas)
    if args.createschemas:
        create_all_schemas()
    uvicorn.run(
        'main:app',
        host=HOST,
        port=PORT,
        reload=True if ENVIRONMENT == 'develop' else False
    )
