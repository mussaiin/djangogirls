import os
import time
import json
import flask
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route("/health")
def health():
    response = flask.jsonify({"status": "ok"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/version")
def version():
    response = flask.jsonify({"version": "1"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/nurlybek-mussin")
def kbtu():
    response = flask.jsonify({"response": "Hello from Nurlybek Mussin!"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/")
def hello():
    response = flask.jsonify({"response": 'Hello world from ' + os.environ["HOSTNAME"] + '!'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/author")
def author():
    response = flask.jsonify({"response": 'This project is made by Nurlybek Mussin.'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    time.sleep(10)
    app.run(host='0.0.0.0', port='80')