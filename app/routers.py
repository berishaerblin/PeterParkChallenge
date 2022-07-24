from datetime import datetime

from flask import Blueprint, request

from database import functions
from database.models import Licences

routes = Blueprint('routes', __name__)


@routes.route('/plate', methods=['GET'])
def fetch_plates():
    response = functions.get_all(Licences)
    return response


@routes.route('/plate', methods=['POST'])
def add_plate():
    plate = request.form.get("plate")
    timestamp = datetime.now()
    response = functions.add_instance(Licences, plate=plate, timestamp=timestamp)
    return response


@routes.route('/search-plate', methods=['GET'])
def search_plate():
    key = request.args.get("key")
    levenshtein = request.args.get("levenshtein")
    response = functions.search_plate(key, levenshtein)
    return response
