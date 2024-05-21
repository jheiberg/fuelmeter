from flask import Flask
from flask import request

import sys
sys.path.append(r'/home/jako/Development/fuelmeter/db')

from insert_fueldata import insert_fuellog
from get_fueldata import get_fuellogs

app = Flask(__name__)

@app.route('/logs', methods=['GET'])
def get_logs():
    return get_fuellogs()

@app.route('/logs', methods=['POST'])
def insert_log():
    return insert_fuellog(request.get_json())

if __name__ == '__main__':
    app.run(debug=True)
