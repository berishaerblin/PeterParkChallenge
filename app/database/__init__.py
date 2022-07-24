from flask_sqlalchemy import SQLAlchemy

from flask import (
    Flask
)


app = Flask(__name__)
app.config.from_object("database.config.Config")
db = SQLAlchemy(app)
