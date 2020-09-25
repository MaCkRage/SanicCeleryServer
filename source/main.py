from flask import Flask
from .database import db
from .routes import page
from .settings import Config
from flask_migrate import Migrate
from flask_admin import Admin


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    app.register_blueprint(page)
    migrate = Migrate(app, db)
    admin = Admin(app, name='garpix', template_mode='bootstrap3')

    return app
