from . import db


class Licences(db.Model):
    __tablename__ = "licences"
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), unique=True)
    timestamp = db.Column(db.DateTime)

    def __init__(self, plate, timestamp):
        self.plate = plate
        self.timestamp = timestamp

    def to_json(self):
        return {
            'plate': self.plate,
            'timestamp': self.timestamp
        }
