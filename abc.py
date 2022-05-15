# from flask import Flask
# from flask import request
# app = Flask(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def hello_world():
#     if request.method == 'POST':
#         return "Method is POST"
#     elif request.method =='GET':
#         return "Method is GET"

# @app.route("/shikhu/")
# def test():
#     return "Hey Stella"



import os
from flask import Flask
from users import user_blueprint
from admin import admin_blueprint
xyz = Flask(__name__)
xyz.register_blueprint(user_blueprint)
xyz.register_blueprint(admin_blueprint)

@xyz.route("/")
def main():
    return "Welcome!"

@xyz.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    xyz.run(host="0.0.0.0", port=5000)