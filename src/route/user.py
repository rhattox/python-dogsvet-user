from flask import Blueprint

user = Blueprint('user', __name__)

@user.route("/user/")
def index():
    return "Hello, this is the main page!"

@user.route("/user/about")
def about():
    return "This is the about page!"