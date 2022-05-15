# from flask import Blueprint, render_template

# user_blueprint = Blueprint('user', __name__)

# @user_blueprint.route("/user/")
# def index():
#     return "Hello This is User Module in My Flask APP"


from flask import Blueprint
user_blueprint = Blueprint('userdtyjgh', __name__)

@user_blueprint.route("/user/")
def qwerty():
    return "Hey, This is my new blueprint"