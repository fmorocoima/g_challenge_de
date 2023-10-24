import os

if not os.getenv('ENVIRONMENT', False):
    from dotenv import load_dotenv
    load_dotenv('g_challenge/.env',)

# Server settings:
ENVIRONMENT = os.getenv('ENVIRONMENT', 'prod')
HOST = '0.0.0.0'
PORT = int(os.getenv('PORT', 8010))


# Database settings:
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('DB_PORT')

print("ENV VARS",ENVIRONMENT,HOST,PORT,POSTGRES_DB,POSTGRES_USER,POSTGRES_PASSWORD,POSTGRES_HOST,DB_PORT)