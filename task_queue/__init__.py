from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from task_queue.config import Config
from flask_mail import Mail


db = SQLAlchemy()
mail = Mail()


def create_app(config_class=Config):
    """
    Binds all necessary objects to app instance, configs with .env
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    from task_queue.app import queue
    app.register_blueprint(queue)

    return app
