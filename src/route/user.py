from flask import Blueprint, request, jsonify
from ..model.user import User

user = Blueprint('user', __name__)

@user.route("/user/")
def index():
    return "Hello, this is the main page!"

@user.route("/user/register", methods=['POST'])
def register():
    data = request.get_json()
    user = User(data["name"], data["email"], data["cpf"], data["password"], data["phone"], data["birthday"])

    # return user.name
    return

@user.route("/user/about")
def about():
    return "This is the about page!"