import os
import uvicorn
from g_challenge_de.src.main import app
from g_challenge_de.src.core.db.create_schemas import create_all_schemas

if __name__ == "__main__":
    create_all_schemas()
    uvicorn.run(
        app,
        host=os.getenv('HOST'),
        port=int(os.getenv('PORT')),
        reload=True if os.getenv('ENVIRONMENT') =='develop' else False
        )