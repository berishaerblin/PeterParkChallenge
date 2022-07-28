import json
import re

from sqlalchemy import text

from . import db


def get_all(model):
    data = model.query.all()
    all_licences = []
    for licence in data:
        structured_licence = {
            "id": licence.id,
            "plate": licence.plate,
            "timestamp": str(licence.timestamp)
        }

        all_licences.append(structured_licence)
    if data:
        return {"data": all_licences}, 200
    else:
        return {"data": "No data!"}, 403


def add(model, **kwargs):
    if not kwargs.get("plate"):
        return json.dumps("Plate field in json is missing!"), 400

    if not re.match(r'^[a-zA-Z]{1,3}-[a-zA-Z]{1,2}[1-9]{1}\d{,3}$', kwargs.get("plate")):
        return json.dumps("Plate is not a valid German plate!"), 422
    else:
        instance = model(**kwargs)
        db.session.add(instance)
        commit_changes()
        return json.dumps("Added to database!"), 200


def search_plate(key, levenshtein):
    sql = text(f"SELECT REPLACE(plate, '-', ''), timestamp FROM licences WHERE levenshtein(plate, '{key}') = {levenshtein}")
    results = db.engine.execute(sql)
    response = []
    if len(results.all()):
        for result in results:
            structured_filter = {
                "plate": result[0],
                "timestamp": str(result[1])
            }
            response.append(structured_filter)
        return {key: response}, 200
    else:
        return{key: "No match!"}, 400


def commit_changes():
    db.session.commit()
