from flask import Flask

def create_app():

    app = Flask(__name__)

    from .blueprints.user import user
    app.register_blueprint(user)

    from .blueprints.api import api
    app.register_blueprint(api)

    return app