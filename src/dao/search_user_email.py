import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from src.model.user import User

load_dotenv()
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_endpoint = os.getenv("POSTGRES_ENDPOINT")
postgres_db = os.getenv("POSTGRES_DB")

db_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_endpoint}/{postgres_db}"
engine = create_engine(db_url, echo=True)


def search_user_email(user):
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    wanted_user = None
    try:
        wanted_user = session.query(User).filter_by(email=user.email).first()
    except Exception as e:
        # Rollback the session in case of an error
        session.rollback()
        print(f"Error: {e}")
        return None
    finally:
        # Close the session
        session.close()
        return wanted_user
