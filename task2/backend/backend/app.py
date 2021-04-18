import os
import time
import json

from flask import Flask

app = Flask(__name__)


@app.route("/health")
def health():
    return '{"status": "ok"}'


@app.route("/version")
def version():
    return '{"version": "1"}'


@app.route("/nurlybek-mussin")
def kbtu():
    return 'Hello from Nurlybek Mussin!'


@app.route("/")
def hello():
    return 'Hello world from ' + os.environ["HOSTNAME"] + '!'


@app.route("/author")
def author():
    return 'This project is made by Nurlybek Mussin.'


if __name__ == "__main__":
    time.sleep(10)
    app.run(host='0.0.0.0', port='80')