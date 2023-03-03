from flask import Flask, jsonify
from yoda.yoda import preach_yoda


app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    """
    Returns the response that the
    you chat gpt api returns, need a
    way to make it so that you can
    only see one unique respones per
    day so that we do not exceed the 
    api requests limit
    """
    return jsonify(preach_yoda())


if __name__ == "__main__":
    app.run()

