Del 2 – Virtual Environments och pip 🐍
> **Kurs:** Virtualiseringsteknik  
> **Syfte:** Lära sig isolera Python-projekt med virtual environments  
> **Miljö:** Windows med Git Bash
---
Innehåll
Vad är pip?
Vad är Flask?
Vad är ett virtual environment?
Skapa och aktivera venv
Installera paket med pip
requirements.txt
---
1. Vad är pip?
`pip` är Pythons pakethanterare – tänk på det som en appbutik för Python.
Python kan inte göra allt själv från början. Men tusentals utvecklare runt om i världen har byggt färdiga verktyg (paket) som du kan ladda ner och använda direkt. Med `pip` laddar du ner dessa paket med ett enda kommando.
```bash
pip install flask        # Installera Flask
pip install requests     # Installera ett annat paket
pip list                 # Visa alla installerade paket
pip show flask           # Visa info om ett specifikt paket
pip uninstall flask      # Ta bort ett paket
```
> 💡 Ungefär som `apt install` på Linux eller App Store på telefonen – fast för Python-kod.
---
2. Vad är Flask?
Flask är ett webbramverk – ett färdigt verktyg för att bygga webbservrar med Python.
Utan Flask skulle du behöva skriva hundratals rader kod bara för att ta emot en webbförfrågan. Med Flask räcker det med några rader:
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hej världen!"
```
Det är allt som behövs för en fungerande webbserver!
Varför används Flask i kursen?
I kursen ska vi:
Skriva en webbapplikation med Flask 🐍
Driftsätta den på två servrar med Ansible ⚙️
Låta nginx fördela trafiken mellan servrarna 🔀
---
3. Vad är ett virtual environment?
Tänk dig att du har två projekt:
Projekt A behöver Flask version 2.0
Projekt B behöver Flask version 3.0
Om du installerar allt globalt på datorn krockar de med varandra.
Ett virtual environment (venv) är som en egen liten låda per projekt – helt isolerad från resten av datorn.
```
Utan venv:                    Med venv:

Systemet                      Systemet
└── Python 3.x                └── Python 3.x (orörd)
    └── Flask 2.0 (globalt)
                              projekt-a/venv/
                              └── Flask 2.0

                              projekt-b/venv/
                              └── Flask 3.0  ← annan version!
```
---
4. Skapa och aktivera venv
Skapa virtual environment
```bash
# Gå till din projektmapp
cd /c/python-projekt

# Skapa venv (skapar en mapp som heter "venv")
python -m venv venv

# Kolla att mappen skapades
ls
# Du ska se: venv/
```
Aktivera venv (Git Bash på Windows)
```bash
source venv/Scripts/activate
```
Du vet att det fungerar när du ser (venv) längst till vänster:
```
(venv) farha@Farre MINGW64 /c/python-projekt
$
```
Inaktivera venv
```bash
deactivate
```
> ⚠️ **Viktigt:** Kom ihåg att alltid aktivera venv innan du jobbar med projektet!
> Annars installeras paket globalt på datorn istället för i projektet.
---
5. Installera paket med pip
När venv är aktiverat installeras allt inuti venv-mappen:
```bash
# Installera Flask
pip install flask

# Kontrollera att det installerades rätt
pip show flask
```
Output från `pip show flask`:
```
Name: Flask
Version: 3.1.3
Location: C:\python-projekt\venv\Lib\site-packages
```
> 💡 Se att `Location` pekar på `venv\Lib\site-packages` – det betyder att
> Flask installerades i venv, inte globalt!
---
6. requirements.txt
`requirements.txt` är en textfil som listar alla paket projektet behöver,
med exakta versionsnummer. Det gör att vem som helst kan återskapa
exakt samma miljö på vilken dator eller server som helst.
Spara dina paket
```bash
pip freeze > requirements.txt
```
Kolla innehållet
```bash
cat requirements.txt
```
Exempel på output:
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
Installera från requirements.txt (på en ny dator/server)
```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
# Alla paket installeras i exakt samma versioner!
```
> 💡 **Tips:** Lägg till `venv/` i din `.gitignore`.
> Virtual environments ska aldrig laddas upp till Git – de är stora,
> plattformsspecifika och kan alltid återskapas från `requirements.txt`.
---
Sammanfattning – snabbreferens
```bash
# Skapa virtual environment
python -m venv venv

# Aktivera (Windows Git Bash)
source venv/Scripts/activate

# Installera paket
pip install flask

# Kolla ett paket
pip show flask

# Lista alla paket
pip list

# Spara beroenden
pip freeze > requirements.txt

# Installera från fil
pip install -r requirements.txt

# Inaktivera venv
deactivate
```
---
Del 2 klar ✅ – Nästa: Del 3 – Miljövariabler och requirements.txt