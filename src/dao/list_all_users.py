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


def list_all_users():
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        dict_list = []
        all_users_list = session.query(User).all()
        for item in all_users_list:
            dict_list.append(item.to_dict())
    except Exception as e:
        # Rollback the session in case of an error
        session.rollback()
        print(f"Error: {e}")
        return None
    finally:
        # Close the session
        session.close()
        return dict_list
