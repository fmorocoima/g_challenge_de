# import os

# if not os.getenv('ENVIRONMENT', False):
#     from dotenv import load_dotenv
#     load_dotenv('g_challenge/.env',)

# Server settings:
ENVIRONMENT = 'prod'
HOST = '0.0.0.0'
PORT = 8020


POSTGRES_HOST = "gchallengedb.postgres.database.azure.com"
POSTGRES_DB = "g_challenge_db_de"
POSTGRES_USER = "user_g_challenge"
POSTGRES_PASSWORD = "Cha12llengeG!"
DB_PORT = 5432


# print("ENV VARS",ENVIRONMENT,HOST,PORT,POSTGRES_DB,POSTGRES_USER,POSTGRES_PASSWORD,POSTGRES_HOST,DB_PORT)