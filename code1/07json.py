from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    data = {
        "name": "liu",
        "age": 24
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(houst="0.0.0.0", prot=8000)