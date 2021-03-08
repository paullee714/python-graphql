from flask import Flask, jsonify
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object((get_flask_env()))

    @app.route("/")
    def test():
        return jsonify({"message": "test Good"})

    return app


def get_flask_env():
    if(Config.ENV == "prod"):
        return 'config.prodConfig'
    elif (Config.ENV == "dev"):
        return 'config.devConfig'
