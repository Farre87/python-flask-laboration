# Python Flask Laboration 🐍

En fullständig webbinfrastruktur byggd med Python, Flask, Ansible och nginx.

## Arkitektur

Webbläsare → nginx (lastbalanserare)
├── web1 (Flask) ──┐
└── web2 (Flask) ──┴── PostgreSQL (databas)

## Tekniker
| Verktyg | Användning |
|---------|-----------|
| Python + Flask | Webbapplikation |
| PostgreSQL | Databas |
| Ansible | Automatisk installation |
| Vagrant + VirtualBox | Virtuella servrar |
| nginx | Lastbalansering |

## API-endpoints
| URL | Beskrivning |
|-----|------------|
| `/` | Visar vilken server som svarar |
| `/info` | JSON med serverinfo |
| `/health` | Hälsokontroll |
| `/meddelanden` GET | Hämta alla meddelanden |
| `/meddelanden` POST | Spara ett meddelande |

## Lärdomar
- Python-grunder och Flask
- Ansible automatisering
- nginx lastbalansering och failover
- PostgreSQL databas

