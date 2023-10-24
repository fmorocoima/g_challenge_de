from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import declarative_base

from g_challenge_de.src.settings import (
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    DB_PORT
    )
# POSTGRES_HOST = "gchallengedb.postgres.database.azure.com"
# POSTGRES_DB = "g_challenge_db_de"
# POSTGRES_USER = "user_g_challenge"
# POSTGRES_PASSWORD = "Cha12llengeG!"
# DB_PORT = 5432


#Configure the connection string (replace the values with your own).
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{DB_PORT}/{POSTGRES_DB}'

# Creates an instance of the SQLAlchemy engine
ENGINE = create_engine(DATABASE_URL)

# Create a session
SESSION = sessionmaker(bind=ENGINE)
session = SESSION()
BASE = declarative_base()

def execute(stmt,engine=ENGINE):
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()
        return result

# Test database health:
def db_health():
    try:
        ENGINE = create_engine(DATABASE_URL)
        connection = ENGINE.connect()
        print("Database connection successful")
        connection.close()
    except OperationalError as e:
        print("Error to connect database:", e)