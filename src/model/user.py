from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))
    cpf: Mapped[str] = mapped_column(String(30))
    phone: Mapped[str] = mapped_column(String(30))
    birthday: Mapped[str] = mapped_column(String(30))

    def __init__(self, name, email, cpf, password, phone, birthday):
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf
        self.phone = phone
        self.birthday = birthday

    def to_dict(self):
        # Convert object attributes to a dictionary
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'cpf': self.cpf,
            'phone': self.phone,
            'birthday': self.birthday,
        }

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r}, phone={self.phone!r}, cpf={self.phone!r}, birthday={self.birthday!r})"
