from flask import Blueprint
admin_blueprint = Blueprint('admin', __name__)
@admin_blueprint.route("/admin/")
def result():
    return "Hey , How are you."