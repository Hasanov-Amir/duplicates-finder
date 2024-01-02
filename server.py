from connexion import FlaskApp
from flask_cors import CORS

app = FlaskApp(__name__)
app.add_api("api.yaml")
CORS(app.app, resources={r"/find-duplicates": {"origins": "*"}})


def run_server(args):
    app.run(host=args["host"], port=args["port"], debug=args["debug"])
