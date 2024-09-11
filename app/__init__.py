from flask import Flask
from flask_migrate import Migrate
from .models import db

from .api.api_v1 import api_v1
from .config import Config

migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize the database and migration
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(api_v1)

    return app
