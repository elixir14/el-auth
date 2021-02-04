from flask import Flask
from .extensions import mongo
from .views import main
from flask_jwt_extended import JWTManager

def create_app(config_object='app.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    jwt = JWTManager(app)

    mongo.init_app(app)

    app.register_blueprint(main)

    return app
