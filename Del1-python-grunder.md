Del 1 – Python Grunder 🐍
> **Kurs:** Virtualiseringsteknik  
> **Syfte:** Lära sig grunderna i Python steg för steg  
> **Miljö:** Windows med Git Bash
---
Innehåll
Vad är Python?
Köra ett Python-skript
print() – skriv ut text
Variabler
input() – fråga användaren
if / elif / else – kontrollflöde
for-loopar
Funktioner med def
return – skicka tillbaka ett värde
f-strings – snygg textformatering
import – använda färdiga moduler
---
1. Vad är Python?
Python är ett tolkningsbart programspråk – det betyder att Python-tolkaren
läser och kör koden rad för rad, utan att kompilera i förväg. Det gör det
enkelt att testa och felsöka.
Kontrollera att Python är installerat:
```bash
python --version
# Exempel på output: Python 3.14.0
```
---
2. Köra ett Python-skript
Ett Python-skript är en textfil som slutar på `.py`.
Skapa och kör ett skript i Git Bash:
```bash
# Gå till din projektmapp
cd /c/python-projekt

# Skapa en ny fil
touch mitt-program.py

# Öppna filen i Notepad
notepad mitt-program.py

# Kör skriptet
python mitt-program.py
```
> ⚠️ **Viktigt:** Skriv bara `python mitt-program.py` i bash.
> Ordet `python` ska INTE skrivas inuti själva filen!
---
3. print() – skriv ut text
`print()` skriver ut text eller värden till terminalen.
Det är det vanligaste sättet att se vad som händer i ett program.
```python
# Skriva ut en enkel text
print("Hej världen!")

# Skriva ut ett tal
print(42)

# Skriva ut flera värden på en rad
print("Servern kör på port", 5000)
```
Output:
```
Hej världen!
42
Servern kör på port 5000
```
---
4. Variabler
En variabel är som en låda där du sparar information.
Du ger lådan ett namn och lägger något i den.
Python räknar automatiskt ut vilken typ det är – du behöver inte ange det.
```python
# Sträng (text)
namn = "Farre"
stad = "Uppsala"

# Heltal (int)
ålder = 20
port  = 5000

# Decimaltal (float)
version = 3.10

# Booleskt värde (sant/falskt)
debug = True
klar  = False

# Lista – flera värden i en variabel
frukter = ["äpple", "banan", "apelsin"]

# Ordbok (dict) – nyckel och värde
konfiguration = {
    "host": "0.0.0.0",
    "port": 5000,
    "debug": False
}

print(namn)               # Farre
print(ålder)              # 20
print(frukter[0])         # äpple  (index börjar på 0!)
print(konfiguration["host"])  # 0.0.0.0
```
Listor – vanliga kommandon
```python
frukter = ["äpple", "banan", "apelsin"]

frukter.append("mango")      # Lägg till i slutet
frukter.remove("banan")      # Ta bort ett värde
print(frukter[0])            # Hämta första värdet
print(len(frukter))          # Hur många finns det?
```
---
5. input() – fråga användaren
`input()` stannar programmet och väntar på att användaren skriver något.
Det som skrivs in sparas i en variabel.
```python
namn = input("Vad heter du? ")
print("Hej " + namn + "!")
```
Output:
```
Vad heter du? Farre
Hej Farre!
```
> 💡 `input()` returnerar alltid en **sträng (text)**.
> Om du vill ha ett tal måste du konvertera med `int()`:
```python
ålder = int(input("Hur gammal är du? "))
print(f"Du är {ålder} år gammal.")
```
---
6. if / elif / else – kontrollflöde
Med `if / elif / else` kan programmet ta beslut och ge olika svar
beroende på vad som stämmer.
> ⚠️ **Viktigt:** Raderna inuti ett if-block måste ha **4 mellanslag** indragning.
> Det är så Python förstår vad som hör ihop.
```python
namn = input("Vad heter du? ")

if namn == "Farre":
    print("Hej Farre, välkommen tillbaka!")
elif namn == "Dorhan":
    print("Hej Dorhan!")
else:
    print("Hej " + namn + ", du är ny här!")
```
Jämförelseoperatorer
Operator	Betydelse
`==`	är lika med
`!=`	är INTE lika med
`>`	större än
`<`	mindre än
`>=`	större än eller lika med
`in`	finns i en lista
```python
port = 5000

if port == 80:
    print("Standard HTTP-port")
elif port == 443:
    print("Standard HTTPS-port")
else:
    print(f"Användardefinierad port: {port}")

# Kolla om något finns i en lista
servrar = ["web1", "web2"]
if "web1" in servrar:
    print("web1 finns i listan")
```
---
7. for-loopar
En `for`-loop upprepar samma kod flera gånger.
```python
# Loop med range() – räkna från 0 till 4
for i in range(5):
    print(f"Detta är rad nummer {i}")

# Output:
# Detta är rad nummer 0
# Detta är rad nummer 1
# Detta är rad nummer 2
# Detta är rad nummer 3
# Detta är rad nummer 4
```
> 💡 Datorer börjar alltid räkna från **0**, inte 1. Det är normalt!
```python
# Loopa igenom en lista
frukter = ["äpple", "banan", "apelsin"]
for frukt in frukter:
    print(frukt)

# Loopa med index (enumerate)
for i, frukt in enumerate(frukter):
    print(f"Frukt {i+1}: {frukt}")
```
Praktiskt exempel – fyll en lista med input
```python
frukter = []  # Tom lista

for i in range(3):
    frukt = input("Skriv in en frukt: ")
    frukter.append(frukt)

print("Din fruktkorg:")
for frukt in frukter:
    print(frukt)
```
---
8. Funktioner med def
En funktion är som ett recept – du skriver koden en gång
och kan sedan använda den hur många gånger som helst.
```python
# Definiera en funktion
def halsa(namn):
    print(f"Hej, {namn}!")

# Anropa funktionen
halsa("Farre")    # Output: Hej, Farre!
halsa("Dorhan")   # Output: Hej, Dorhan!
halsa("Python")   # Output: Hej, Python!
```
Funktion med flera parametrar
```python
def starta_server(host, port):
    print(f"Startar server på {host}:{port}")

starta_server("0.0.0.0", 5000)
# Output: Startar server på 0.0.0.0:5000
```
Funktion med standardvärden
```python
# Om inget skickas in används standardvärdet
def starta_server(host="0.0.0.0", port=5000, debug=False):
    print(f"Startar på {host}:{port} (debug={debug})")

starta_server()                    # Startar på 0.0.0.0:5000 (debug=False)
starta_server(port=8080, debug=True)  # Startar på 0.0.0.0:8080 (debug=True)
```
---
9. return – skicka tillbaka ett värde
Med `return` kan en funktion räkna ut något och skicka tillbaka svaret
så att du kan använda det vidare i koden.
```python
def addera(a, b):
    return a + b

svar = addera(3, 4)
print(f"3 + 4 = {svar}")           # 3 + 4 = 7
print(f"10 + 20 = {addera(10, 20)}")  # 10 + 20 = 30
```
Skillnad mellan print och return
```python
# print() i funktion – skriver ut men värdet försvinner
def med_print(a, b):
    print(a + b)

# return – skickar tillbaka värdet så du kan spara det
def med_return(a, b):
    return a + b

resultat = med_return(5, 3)
print(f"Svaret är: {resultat}")  # Svaret är: 8
```
Return med villkor (skydda mot fel)
```python
def dela(a, b):
    if b == 0:
        return None   # Avbryt om division med noll
    return a / b

print(dela(10, 2))   # 5.0
print(dela(10, 0))   # None
```
---
10. f-strings – snygg textformatering
f-strings är det enklaste sättet att bädda in variabler i text.
Sätt ett `f` framför citattecknet och skriv variabelnamnet i `{ }`.
```python
namn  = "Farre"
ålder = 20
stad  = "Uppsala"

# Gammalt sätt (krångligt med +)
print("Hej " + namn + "! Du är " + str(ålder) + " år.")

# Med f-string (mycket enklare!)
print(f"Hej {namn}! Du är {ålder} år och bor i {stad}.")
```
Beräkningar direkt i f-strings
```python
pris  = 100
antal = 3

print(f"Du köpte {antal} saker.")
print(f"Totalt kostar det {pris * antal} kr.")
# Output: Totalt kostar det 300 kr.
```
f-strings används överallt i kursen
```python
hostname = "web1"
port     = 5000

print(f"Servern {hostname} lyssnar på port {port}")
# Output: Servern web1 lyssnar på port 5000
```
---
11. import – använda färdiga moduler
Python har ett stort bibliotek av färdiga verktyg (moduler).
Du importerar dem med `import` – ingen installation behövs.
```python
import os
import socket

# Vilket operativsystem kör du?
# nt = Windows, posix = Linux/Mac
print(f"OS: {os.name}")

# Vad heter datorn/servern?
hostname = socket.gethostname()
print(f"Datorns namn: {hostname}")
```
Importera specifika delar
```python
from datetime import datetime
from os import getenv

nu = datetime.now()
print(f"Tidsstämpel: {nu.isoformat()}")
```
Vanliga moduler i kursen
Modul	Används till
`os`	Operativsystem, miljövariabler
`socket`	Nätverksinformation (hostname etc.)
`datetime`	Datum och tid
`flask`	Webbserver (installeras med pip)
---
Sammanfattning – snabbreferens
```python
# print
print("Hej!")
print(f"Hej {namn}!")

# Variabler
namn    = "Farre"
ålder   = 20
frukter = ["äpple", "banan"]

# input
svar = input("Fråga: ")
tal  = int(input("Skriv ett tal: "))

# if / elif / else
if x == 1:
    print("ett")
elif x == 2:
    print("två")
else:
    print("annat")

# for-loop
for i in range(5):
    print(i)

for frukt in frukter:
    print(frukt)

# Funktion
def halsa(namn):
    print(f"Hej {namn}!")

def addera(a, b):
    return a + b

# import
import os
import socket
hostname = socket.gethostname()
```
---
Del 1 klar ✅ – Nästa: Del 2 – Virtual environments och pip