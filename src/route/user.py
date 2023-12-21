import json

from flask import Blueprint, request, jsonify, make_response
from ..model.user import User

user = Blueprint('user', __name__)


@user.route("/user/", methods=['GET'])
def index():
    data_dict = {
        "name": "Bruno",
        "email": "bruno@gmail.com",
        "cpf": "123123123",
        "password": "password123",
        "phone": "123453467",
        "birthday": "1990-12-03"
    }

    return jsonify(data_dict)


@user.route("/user/register", methods=['POST'])
def register():
    data = request.get_json()
    user = User(name=data["name"], email=data["email"], cpf=data["cpf"], password=data["password"], phone=data["phone"],
                birthday=data["birthday"])
    from src.dao.create_user import create_user
    response_function = create_user(user)
    if response_function:
        return "OK"
    else:
        return "FAILED"


@user.route("/user/list/all", methods=['GET'])
def list_all_users():
    from src.dao.list_all_users import list_all_users
    response_function = list_all_users()

    if not response_function or response_function is None:
        return "No Users Found!"

    return jsonify(response_function)


@user.route("/user/search/email", methods=['POST'])
def search_user_email():
    from src.dao.search_user_email import search_user_email
    data = request.get_json()
    user = User(name=None, email=data["email"], cpf=None, password=None, phone=None,
                birthday=None)

    response_function = search_user_email(user)

    if response_function is None:
        return "No user found!"

    return jsonify(response_function.to_dict())


@user.route("/user/delete/email", methods=['POST'])
def delete_user_email():
    from src.dao.delete_user import delete_user
    data = request.get_json()
    user = User(name=None, email=data["email"], cpf=None, password=None, phone=None,
                birthday=None)

    response_function = delete_user(user)

    print(response_function)
    if response_function:
        return "User deleted successfully!"
    else:
        return "Not exists"
