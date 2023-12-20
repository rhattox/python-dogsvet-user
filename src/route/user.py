from flask import Blueprint, request, jsonify, make_response
from ..model.user import User

user = Blueprint('user', __name__)


@user.route("/user/")
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
