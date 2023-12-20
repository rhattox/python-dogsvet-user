import os
import sys
from dotenv import load_dotenv

def load_database_environment_variables():
    # Access environment variables
    load_dotenv()

    postgres_endpoint = os.getenv("POSTGRES_ENDPOINT")

    postgres_user = os.getenv("POSTGRES_USER")

    postgres_password = os.getenv("POSTGRES_PASSWORD")

    postgres_db = os.getenv("POSTGRES_DB")

    ENV_LIST = (postgres_endpoint,postgres_user,postgres_password,postgres_db)

    for item in ENV_LIST:
        check_none_value(item)

    print("Database Variables Loaded!")


def check_none_value(environment_variable):
    if environment_variable is None:
        print(f"The variable {environment_variable} is None.")
        sys.exit(1)
