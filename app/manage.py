from flask.cli import FlaskGroup
from sqlalchemy import text

from routers import routes
from database import db, app

cli = FlaskGroup(app)


@cli.command("create_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    extension = text("CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;")
    db.engine.execute(extension)


if __name__ == "__main__":
    app.register_blueprint(routes)
    cli()

