from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return f"Hej från {socket.gethostname()}!"

@app.route("/info")
def info():
    return jsonify({
        "hostname":  socket.gethostname(),
        "timestamp": datetime.now().isoformat(),
        "port":      os.environ.get("PORT", "5000"),
        "db_host":   os.environ.get("DB_HOST", "ej konfigurerad")
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok", "server": socket.gethostname()}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
