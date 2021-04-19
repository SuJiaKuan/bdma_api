from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_restful import Api

from config import Config
from errors import errors
from models import db
from resources import AssignmentSubmission
from resources import MidtermSubmission


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Extensions.
CORS(app)


@app.errorhandler(404)
def not_found_callback(e):
    return jsonify(errors["EndpointNotFound"]), 404


@app.errorhandler(405)
def not_allowed_callback(e):
    return jsonify(errors["MethodNotAllowed"]), 405


@app.errorhandler(Exception)
def server_error_callback(e):
    return jsonify(errors["ServerError"]), 500


api = Api(
    app,
    prefix="/{}".format(app.config["API_VERSION"]),
    errors=errors,
)

api.add_resource(AssignmentSubmission, "/assignments")
api.add_resource(MidtermSubmission, "/midterm")
