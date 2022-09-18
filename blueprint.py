from flask import Blueprint

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route(f"/hello-world-12")
def hello_world():
    return f"Hello World 12"
