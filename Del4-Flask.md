Del 4 – Flask 🌐
> **Kurs:** Virtualiseringsteknik  
> **Syfte:** Lära sig bygga en webbserver med Python och Flask  
> **Miljö:** Windows med Git Bash
---
Innehåll
Vad är Flask?
Din första Flask-app
Routes – olika adresser
Routes med variabel
JSON-svar med jsonify
app.run() – host och port
Färdig Flask-app för kursen
---
1. Vad är Flask?
Flask är ett webbramverk – det gör att din Python-kod kan svara på
riktiga webbförfrågningar.
När du går in på en webbsida i webbläsaren:
Webbläsaren skickar en förfrågan till en server
Servern svarar med text, JSON eller HTML
Flask hanterar hela den processen åt dig
Flask installeras med pip:
```bash
pip install flask
```
---
2. Din första Flask-app
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hej från Flask!"

if __name__ == "__main__":
    app.run()
```
Kör:
```bash
python mitt-program.py
```
Output:
```
* Serving Flask app 'mitt-program'
* Running on http://127.0.0.1:5000
```
Öppna webbläsaren och gå till `http://127.0.0.1:5000` – du ser "Hej från Flask!"
> 💡 Stoppa Flask med `Ctrl + C` i bash när du är klar.
> ⚠️ Kom ihåg att **aktivera venv** innan du kör Flask:
> `source venv/Scripts/activate`
---
3. Routes – olika adresser
En route är en koppling mellan en URL-adress och en Python-funktion.
När någon besöker den adressen körs funktionen och svaret skickas tillbaka.
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hej från Flask!"

@app.route("/info")
def info():
    return "Det här är info-sidan!"

@app.route("/health")
def health():
    return "Servern mår bra!"

if __name__ == "__main__":
    app.run()
```
URL	Svar
`http://127.0.0.1:5000/`	Hej från Flask!
`http://127.0.0.1:5000/info`	Det här är info-sidan!
`http://127.0.0.1:5000/health`	Servern mår bra!
---
4. Routes med variabel
Med `<variabelnamn>` i route-mönstret kan Flask ta emot vad som helst
från URL:en och skicka det vidare till funktionen.
```python
@app.route("/halsa/<namn>")
def halsa(namn):
    return f"Hej {namn}, välkommen!"
```
Hur det fungerar:
```
URL:      /halsa/Farre
Mönster:  /halsa/<namn>
Resultat: namn = "Farre"  →  "Hej Farre, välkommen!"

URL:      /halsa/Dorhan
Mönster:  /halsa/<namn>
Resultat: namn = "Dorhan" →  "Hej Dorhan, välkommen!"
```
Flask vet inte namnen i förväg – den tar bara emot vad du skickar!
---
5. JSON-svar med jsonify
`jsonify()` omvandlar en Python-ordbok till ett korrekt JSON-svar.
JSON är standardformatet när servrar pratar med varandra.
```python
from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "status":   "ok"
    })
```
Output i webbläsaren:
```json
{
    "hostname": "Farre",
    "status": "ok"
}
```
Health check – viktigt för nginx!
```python
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200
```
> 💡 `/health` används av nginx lastbalanseraren för att kolla om
> Flask-servern lever. Om den inte svarar slutar nginx skicka trafik dit!
```
nginx → /health? → Flask svarar "ok" ✅ → skicka trafik hit
                 → Flask svarar inte  ❌ → skippa denna server
```
---
6. app.run() – host och port
```python
# Lyssnar bara på localhost – inte nåbar från andra maskiner
app.run()

# Lyssnar på alla nätverksgränssnitt – nåbar från andra maskiner
app.run(host="0.0.0.0")

# Med port från miljövariabel
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```
> ⚠️ **Viktigt:** I kursen måste Flask lyssna på `0.0.0.0` – annars
> kan inte nginx nå Flask-servern från en annan VM!
---
7. Färdig Flask-app för kursen
Det här är den kompletta app.py som används i laborationen:
```python
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
```
Testa alla endpoints:
URL	Svar
`http://127.0.0.1:5000/`	Hej från Farre!
`http://127.0.0.1:5000/info`	JSON med hostname, tid, port
`http://127.0.0.1:5000/health`	`{"status": "ok"}`
---
Sammanfattning – snabbreferens
```python
from flask import Flask, jsonify
import os, socket
from datetime import datetime

app = Flask(__name__)

# Enkel route
@app.route("/")
def index():
    return "text"

# Route med variabel
@app.route("/halsa/<namn>")
def halsa(namn):
    return f"Hej {namn}!"

# JSON-svar
@app.route("/info")
def info():
    return jsonify({"nyckel": "värde"})

# Health check
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

# Starta med miljövariabel för port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```
```bash
# Kör Flask
python mitt-program.py

# Stoppa Flask
Ctrl + C
```
---
Del 4 klar ✅ – Nästa: Del 5 – Driftsätta Flask på VMs med nginx