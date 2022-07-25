from flask.cli import FlaskGroup

from routers import routes
from database import db, app

cli = FlaskGroup(app)


@cli.command("create_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    app.register_blueprint(routes)
    cli()

