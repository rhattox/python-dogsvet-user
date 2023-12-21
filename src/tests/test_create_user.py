import unittest
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.model.user import User
from dotenv import load_dotenv

load_dotenv()
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_USER")
postgres_endpoint = os.getenv("POSTGRES_ENDPOINT")
postgres_db = os.getenv("POSTGRES_DB")

db_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_endpoint}/{postgres_db}"
engine = create_engine(db_url, echo=True)

data_dict = {
    "name": "user1",
    "email": "user123@gmail.com",
    "cpf": "12345567788",
    "password": "strongPassword0",
    "phone": "99999999999",
    "birthday": "2000-10-05"
}


class TestUserCreation(unittest.TestCase):

    def test_create_user(self):
        try:
            # Create a session to interact with the database
            Session = sessionmaker(bind=engine)
            session = Session()
            User.metadata.create_all(engine)

            new_user = User(name="user1", email="user123@gmail.com", cpf="12345567788",
                            password="strongPassword0", phone="99999999999", birthday="2000-10-05")

            session.add(new_user)
            # Commit the session to persist the user in the database
            session.commit()
            queried_user = session.query(User).filter_by(email="user123@gmail.com").first()

            self.assertIsNotNone(queried_user)
            self.assertEqual(queried_user.name, name="user1")
            self.assertEqual(queried_user.password, password="strongPassword0")

        except Exception as e:
            # Rollback the session in case of an error
            session.rollback()
            print(f"Error: {e}")

        finally:
            queried_user_delete = session.query(User).filter_by(email="user123@gmail.com").first()
            print(queried_user_delete)
            user_to_delete = session.query(User).filter_by(id=queried_user_delete.id).first()
            session.delete(user_to_delete)
            session.commit()
            session.close()


if __name__ == '__main__':
    unittest.main()
