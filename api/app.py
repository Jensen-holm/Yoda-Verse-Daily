from flask import Flask, jsonify
from yoda.yoda import preach_yoda


app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    return jsonify(preach_yoda())


if __name__ == "__main__":
    app.run()

