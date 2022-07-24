from flask.cli import FlaskGroup

from routers import routes
from database import db, app

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


# @cli.command("seed_db")
# def seed_db():
#     db.session.add(Licence(plate="example", timestamp="2022-07-25"))
#     db.session.commit()


if __name__ == "__main__":
    app.register_blueprint(routes)
    cli()

