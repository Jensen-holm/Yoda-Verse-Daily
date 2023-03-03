from flask import Flask
from yoda.yoda import preach_yoda


app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    r = yoda.preach_yoda()
    print(r)
    return r

if __name__ == "__main__":
    app.run()

