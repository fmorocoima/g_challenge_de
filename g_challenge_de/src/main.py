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

description = '''
## Api challenge for data engineer position at globant
'''
app = FastAPI(
    title="G-challenge data engineering API service docs page", 
    description=description, 
    contact={
        "name": "Freddy Morocoima",
        "url": "https://github.com/fmorocoima/g_challenge_de",
        "email": "morocoimafreddy@gmail.com",
    }
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
