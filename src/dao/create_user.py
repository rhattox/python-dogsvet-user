from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

def create_user(create_new_user):
    load_dotenv()
    postgres_user = os.getenv("POSTGRES_USER")
    postgres_password = os.getenv("POSTGRES_PASSWORD")
    postgres_endpoint = os.getenv("POSTGRES_ENDPOINT")
    postgres_db = os.getenv("POSTGRES_DB")

    db_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_endpoint}/{postgres_db}"
    engine = create_engine(db_url, echo=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add the user to the session
    session.add(create_new_user)

    # Commit the session to persist the user in the database
    session.commit()