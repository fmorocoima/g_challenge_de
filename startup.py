import os
import uvicorn
from g_challenge_de.src.main import app
from g_challenge_de.src.core.db.create_schemas import create_all_schemas
from g_challenge_de.src.settings import (
    ENVIRONMENT, HOST, PORT
)

if __name__ == "__main__":
    create_all_schemas()
    uvicorn.run(
        app,
        host=HOST,
        port=PORT,
        reload=True if ENVIRONMENT =='develop' else False
        )