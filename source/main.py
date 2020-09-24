from flask import Flask
from .database import db
# from .routes import short
from .settings import Config
from flask_migrate import Migrate


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    # app.register_blueprint(short)
    migrate = Migrate(app, db)

    return app
