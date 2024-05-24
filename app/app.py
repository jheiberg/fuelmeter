from flask import Flask, request

from app.db.get_fueldata import get_fuellogs
from app.db.insert_fueldata import insert_fuellog

app = Flask(__name__)


@app.route("/logs", methods=["GET"])
def get_logs():
    return get_fuellogs()


@app.route("/logs", methods=["POST"])
def insert_log():
    return insert_fuellog(request.get_json())


if __name__ == "__main__":
    app.run(debug=True)
