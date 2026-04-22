Del 3 – Miljövariabler och requirements.txt 🌍
> **Kurs:** Virtualiseringsteknik  
> **Syfte:** Lära sig konfigurera program med miljövariabler  
> **Miljö:** Windows med Git Bash
---
Innehåll
Vad är en miljövariabel?
Sätta miljövariabler i bash
Läsa miljövariabler i Python
Standardvärden
Konvertera till rätt typ
requirements.txt
---
1. Vad är en miljövariabel?
En miljövariabel är en inställning som sparas i terminalen – inte i koden.
Det betyder att du kan ändra hur programmet beter sig utan att röra koden.
Varför är det bra?
Samma kod kan köras med olika inställningar på olika servrar
Känslig information (lösenord, nycklar) behöver inte skrivas i koden
Enkelt att byta port, databas eller host utan att öppna filen
```
Utan miljövariabler:          Med miljövariabler:
port = 5000  ← hårdkodat      port = os.environ.get("PORT", "5000")
                               ↑ läser från terminalen istället
```
---
2. Sätta miljövariabler i bash
```bash
# Sätta en miljövariabel
export PORT=5000
export DB_HOST=192.168.56.12
export DB_PASSWORD=hemligt123

# Kontrollera att den är satt
echo $PORT        # Output: 5000
echo $DB_HOST     # Output: 192.168.56.12

# Se alla miljövariabler
env

# Sätta variabel enbart för ett enstaka kommando
PORT=8080 python mitt-program.py
# PORT är bara 8080 under just detta kommandots körning
```
> ⚠️ **Viktigt:** Miljövariabler satta med `export` försvinner när du
> stänger terminalen! De gäller bara för den aktuella sessionen.
---
3. Läsa miljövariabler i Python
Använd modulen `os` för att läsa miljövariabler i Python:
```python
import os

# Läs en miljövariabel
port    = os.environ.get("PORT", "5000")
db_host = os.environ.get("DB_HOST", "localhost")

print(f"Port:    {port}")
print(f"DB Host: {db_host}")
```
Output när variablerna är satta:
```
Port:    5000
DB Host: 192.168.56.12
```
Output när variablerna INTE är satta:
```
Port:    5000      ← standardvärde används
DB Host: localhost ← standardvärde används
```
---
4. Standardvärden
`.get("VARIABELNAMN", "standardvärde")` fungerar så här:
Om variabeln finns → använd dess värde
Om variabeln saknas → använd standardvärdet
```python
import os

# PORT finns → använd dess värde
# PORT saknas → använd "5000"
port = os.environ.get("PORT", "5000")

# Obligatorisk variabel – kraschar om den saknas
# (bra för saker som MÅSTE vara satta)
db_password = os.environ["DB_PASSWORD"]
```
---
5. Konvertera till rätt typ
Miljövariabler är alltid text (str) – även om du satte ett tal.
Om du ska använda värdet som ett tal måste du konvertera:
```python
import os

# Utan konvertering – port är texten "5000"
port_text = os.environ.get("PORT", "5000")

# Med konvertering – port är talet 5000
port_int = int(os.environ.get("PORT", "5000"))

print(type(port_text))   # <class 'str'>
print(type(port_int))    # <class 'int'>
```
Typisk konfiguration för Flask
```python
import os

HOST     = os.environ.get("HOST", "0.0.0.0")
PORT     = int(os.environ.get("PORT", 5000))       # int!
DEBUG    = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
DB_HOST  = os.environ.get("DB_HOST", "localhost")
DB_NAME  = os.environ.get("DB_NAME", "mydb")
DB_PASS  = os.environ.get("DB_PASSWORD", "")
```
> 💡 **PORT måste vara `int`** när Flask startar servern – annars kraschar det!
---
6. requirements.txt
`requirements.txt` listar alla paket projektet behöver med exakta versioner.
Det gör att vem som helst kan återskapa exakt samma miljö.
Spara dina paket
```bash
pip freeze > requirements.txt
```
Exempel på requirements.txt
```
blinker==1.9.0
click==8.3.2
colorama==0.4.6
Flask==3.1.3
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
Werkzeug==3.1.8
```
Installera från requirements.txt
```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
---
Sammanfattning – snabbreferens
```bash
# Sätta miljövariabler i bash
export PORT=5000
export DB_HOST=192.168.56.12

# Kolla en variabel
echo $PORT
```
```python
import os

# Läsa med standardvärde
port    = os.environ.get("PORT", "5000")
db_host = os.environ.get("DB_HOST", "localhost")

# Konvertera till heltal
port = int(os.environ.get("PORT", 5000))

# Typisk Flask-konfiguration
HOST  = os.environ.get("HOST", "0.0.0.0")
PORT  = int(os.environ.get("PORT", 5000))
DEBUG = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
```
---
Del 3 klar ✅ – Nästa: Del 4 – Flask