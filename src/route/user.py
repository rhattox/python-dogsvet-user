from flask import Blueprint, request
from ..model.user import User

user = Blueprint('user', __name__)

@user.route("/user/")
def index():
    return "Hello, this is the main page!"

@user.route("/user/register", methods=['POST'])
def register():
    data = request.get_json()
    user = User(name=data["name"], email=data["email"], cpf=data["cpf"], password=data["password"], phone=data["phone"], birthday=data["birthday"])
    from src.dao.create_user import create_user
    create_user(user)
    # return user.name
    return

@user.route("/user/about")
def about():
    return "This is the about page!"