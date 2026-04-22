from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

@app.route("/")
def index():
    return f"Hej från {socket.gethostname()}!"

@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "port":     os.environ.get("PORT", "5000"),
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)