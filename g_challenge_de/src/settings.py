import os

env_file_path = 'g_challenge_de/.env'

if not os.getenv('ENVIRONMENT', False):
    from dotenv import load_dotenv
    # load_dotenv('g_challenge_de/.env',)
    if os.path.isfile(env_file_path):
        load_dotenv(env_file_path)
    else:
        print(f"the file {env_file_path} no found")

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