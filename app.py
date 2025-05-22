# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)
latest_data = {}

@app.route("/send", methods=["POST"])
def send():
    global latest_data
    latest_data = request.get_json()
    return {"status": "received"}

@app.route("/get", methods=["GET"])
def get():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)