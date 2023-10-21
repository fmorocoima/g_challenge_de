import uvicorn
import argparse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

parser = argparse.ArgumentParser()
parser.add_argument('--createschemas', type=bool, required=False)

description = f'''<a href="https://github.com/fmorocoima/g_challenge_de">
    <img width=10% src="https://static.vecteezy.com/system/resources/previews/016/833/872/original/github-logo-git-hub-icon-on-white-background-free-vector.jpg"/> Follow...</a>'''

app = FastAPI(
    title="G-challenge data engineering API service docs page",
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

@app.get("/")
async def root():
    return {"message": "API Running"}

if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host="0.0.0.0",
        port=8001,
        reload=True
        )
