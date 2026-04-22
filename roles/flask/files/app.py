from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import socket
from datetime import datetime

app = Flask(__name__)

# Koppla till PostgreSQL
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://"
    f"{os.environ.get('DB_USER', 'flaskuser')}:"
    f"{os.environ.get('DB_PASSWORD', 'flask123')}@"
    f"{os.environ.get('DB_HOST', '192.168.56.13')}/"
    f"{os.environ.get('DB_NAME', 'flaskdb')}"
)

db = SQLAlchemy(app)

# Tabell i databasen
class Meddelande(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    text    = db.Column(db.String(200))
    server  = db.Column(db.String(50))
    tid     = db.Column(db.DateTime, default=datetime.now)

# Skapa tabellen automatiskt
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return f"Hej från {socket.gethostname()}!"

@app.route("/info")
def info():
    return jsonify({
        "hostname":  socket.gethostname(),
        "timestamp": datetime.now().isoformat(),
        "port":      os.environ.get("PORT", "5000"),
        "db_host":   os.environ.get("DB_HOST", "192.168.56.13")
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok", "server": socket.gethostname()}), 200

@app.route("/meddelanden", methods=["GET"])
def hamta_meddelanden():
    alla = Meddelande.query.all()
    return jsonify([{
        "id":     m.id,
        "text":   m.text,
        "server": m.server,
        "tid":    m.tid.isoformat()
    } for m in alla])

@app.route("/meddelanden", methods=["POST"])
def spara_meddelande():
    data = request.get_json()
    nytt = Meddelande(
        text=data["text"],
        server=socket.gethostname()
    )
    db.session.add(nytt)
    db.session.commit()
    return jsonify({"status": "sparat", "server": socket.gethostname()}), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)