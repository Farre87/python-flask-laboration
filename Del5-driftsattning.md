Del 5 – Driftsätta Flask på VMs med nginx 🚀

> \*\*Kurs:\*\* Virtualiseringsteknik  

> \*\*Syfte:\*\* Driftsätta Flask på två servrar med nginx lastbalansering  

> \*\*Miljö:\*\* Windows med Git Bash, WSL och VirtualBox

\---

Innehåll

Arkitektur – hur hänger allt ihop?

Vagrant – skapa VMs

WSL – Linux på Windows

Ansible – automatisera installationer

Mappstrukturen

Alla filer förklarade

Kör playbooken

Verifiera och testa

\---

1\. Arkitektur – hur hänger allt ihop?

```

Din laptop (Windows)

&#x20;       │ http://localhost:8080

&#x20;       ↓

&#x20;  nginx VM (192.168.56.10)

&#x20;  Lastbalanserare – delar trafiken jämnt

&#x20;       ↓              ↓

&#x20; Flask VM 1      Flask VM 2

&#x20; 192.168.56.11   192.168.56.12

&#x20; hostname: web1  hostname: web2

```

Tre servrar:

nginx – tar emot alla förfrågningar och delar dem jämnt mellan web1 och web2

web1 – kör Flask-applikationen

web2 – kör Flask-applikationen (kopia av web1)

Round-robin lastbalansering:

```

Förfrågan 1 → web1

Förfrågan 2 → web2

Förfrågan 3 → web1

Förfrågan 4 → web2

```

\---

2\. Vagrant – skapa VMs

Vagrantfile

Vagrantfile beskriver hur VMs ska skapas. Den läggs i projektmappen.

```ruby

NGINX\_IP = "192.168.56.10"

WEB1\_IP  = "192.168.56.11"

WEB2\_IP  = "192.168.56.12"



Vagrant.configure("2") do |config|

&#x20; config.vm.box = "ubuntu/jammy64"



&#x20; config.vm.define "nginx" do |n|

&#x20;   n.vm.hostname = "nginx"

&#x20;   n.vm.network "private\_network", ip: NGINX\_IP

&#x20;   n.vm.network "forwarded\_port", guest: 80, host: 8080

&#x20;   n.vm.provider "virtualbox" do |vb|

&#x20;     vb.memory = 512; vb.cpus = 1

&#x20;   end

&#x20; end



&#x20; config.vm.define "web1" do |w|

&#x20;   w.vm.hostname = "web1"

&#x20;   w.vm.network "private\_network", ip: WEB1\_IP

&#x20;   w.vm.provider "virtualbox" do |vb|

&#x20;     vb.memory = 512; vb.cpus = 1

&#x20;   end

&#x20; end



&#x20; config.vm.define "web2" do |w|

&#x20;   w.vm.hostname = "web2"

&#x20;   w.vm.network "private\_network", ip: WEB2\_IP

&#x20;   w.vm.provider "virtualbox" do |vb|

&#x20;     vb.memory = 512; vb.cpus = 1

&#x20;   end

&#x20; end

end

```

Vagrant-kommandon

```bash

\# Starta alla VMs

vagrant up



\# Kolla status

vagrant status



\# SSH in på en VM

vagrant ssh web1



\# Stoppa alla VMs

vagrant halt



\# Ta bort alla VMs

vagrant destroy

```

\---

3\. WSL – Linux på Windows

WSL (Windows Subsystem for Linux) är en riktig Linux-terminal inuti Windows.

Ansible fungerar bara på Linux – därför använder vi WSL.

Installera WSL och Ubuntu

```powershell

\# Kör i PowerShell som administratör

wsl --install -d Ubuntu

```

Öppna WSL

Sök på "Ubuntu" i startmenyn.

Gå till projektmappen i WSL

```bash

cd /mnt/c/python-projekt

```

> 💡 I WSL är Windows C-disken tillgänglig som `/mnt/c/`

Kopiera och klistra in i WSL

Klistra in: Högerklicka med musen eller `Ctrl + Shift + V`

\---

4\. Ansible – automatisera installationer

Ansible är ett verktyg för att automatiskt installera och konfigurera servrar.

Istället för att manuellt SSH:a in på varje server och köra kommandon,

skriver du instruktioner i YAML-filer och Ansible gör allt åt dig.

Installera Ansible i WSL

```bash

sudo apt update

sudo apt install ansible sshpass -y

```

Kolla versionen

```bash

ansible --version

```

inventory.ini – lista över servrar

```ini

\[nginx]

192.168.56.10 ansible\_user=vagrant ansible\_ssh\_private\_key\_file=/mnt/c/python-projekt/.vagrant/machines/nginx/virtualbox/private\_key



\[webservers]

192.168.56.11 ansible\_user=vagrant ansible\_ssh\_private\_key\_file=/mnt/c/python-projekt/.vagrant/machines/web1/virtualbox/private\_key

192.168.56.12 ansible\_user=vagrant ansible\_ssh\_private\_key\_file=/mnt/c/python-projekt/.vagrant/machines/web2/virtualbox/private\_key

```

Lägg till SSH-nycklar

```bash

mkdir -p \~/.ssh

chmod 700 \~/.ssh

ssh-keyscan -H 192.168.56.10 >> \~/.ssh/known\_hosts

ssh-keyscan -H 192.168.56.11 >> \~/.ssh/known\_hosts

ssh-keyscan -H 192.168.56.12 >> \~/.ssh/known\_hosts

```

Testa anslutning

```bash

ansible all -i inventory.ini -m ping

```

Alla ska svara `pong` ✅

\---

5\. Mappstrukturen

```

python-projekt/

├── Vagrantfile                          ← beskriver VMs

├── inventory.ini                        ← lista över servrar

├── site.yml                             ← huvudfilen Ansible kör

├── vars/

│   └── main.yml                         ← gemensamma variabler

└── roles/

&#x20;   ├── flask/                           ← Flask-rollen (web1, web2)

&#x20;   │   ├── tasks/main.yml               ← vad som ska göras

&#x20;   │   ├── handlers/main.yml            ← körs när något ändras

&#x20;   │   ├── templates/flask.service.j2   ← systemd-tjänstmall

&#x20;   │   ├── files/app.py                 ← Flask-applikationen

&#x20;   │   ├── files/requirements.txt       ← Python-paket

&#x20;   │   └── defaults/main.yml            ← standardvärden

&#x20;   └── nginx/                           ← nginx-rollen (lastbalanseraren)

&#x20;       ├── tasks/main.yml               ← vad som ska göras

&#x20;       ├── handlers/main.yml            ← körs när något ändras

&#x20;       └── templates/nginx.conf.j2      ← nginx-konfigurationsmall

```

\---

6\. Alla filer förklarade

vars/main.yml

Gemensamma variabler som används av båda rollerna:

```yaml

flask\_port: 5000

app\_dir:    /opt/flask

app\_user:   vagrant

```

roles/flask/files/app.py

Flask-applikationen som körs på web1 och web2:

```python

from flask import Flask, jsonify

import os, socket

from datetime import datetime



app = Flask(\_\_name\_\_)



@app.route("/")

def index():

&#x20;   return f"Hej från {socket.gethostname()}!"



@app.route("/info")

def info():

&#x20;   return jsonify({

&#x20;       "hostname":  socket.gethostname(),

&#x20;       "timestamp": datetime.now().isoformat(),

&#x20;       "port":      os.environ.get("PORT", "5000"),

&#x20;       "db\_host":   os.environ.get("DB\_HOST", "ej konfigurerad")

&#x20;   })



@app.route("/health")

def health():

&#x20;   return jsonify({"status": "ok", "server": socket.gethostname()}), 200



if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   port = int(os.environ.get("PORT", 5000))

&#x20;   app.run(host="0.0.0.0", port=port)

```

roles/flask/files/requirements.txt

```

flask==3.1.3

gunicorn==21.2.0

```

roles/flask/defaults/main.yml

```yaml

app\_dir:  /opt/flask

app\_user: vagrant

app\_port: 5000

```

roles/flask/tasks/main.yml

Instruktioner för att installera Flask på web1 och web2:

```yaml

\---

\- name: Install Python 3 and pip

&#x20; apt:

&#x20;   name: \[python3, python3-pip, python3-venv]

&#x20;   state: present

&#x20;   update\_cache: yes



\- name: Create application directory

&#x20; file:

&#x20;   path: "{{ app\_dir }}"

&#x20;   state: directory

&#x20;   owner: "{{ app\_user }}"

&#x20;   mode: "0755"



\- name: Copy application files

&#x20; copy:

&#x20;   src: "{{ item }}"

&#x20;   dest: "{{ app\_dir }}/{{ item }}"

&#x20;   owner: "{{ app\_user }}"

&#x20; loop:

&#x20;   - app.py

&#x20;   - requirements.txt

&#x20; notify: restart flask



\- name: Create virtual environment

&#x20; command:

&#x20;   cmd: python3 -m venv {{ app\_dir }}/venv

&#x20;   creates: "{{ app\_dir }}/venv"



\- name: Install dependencies from requirements.txt

&#x20; pip:

&#x20;   requirements: "{{ app\_dir }}/requirements.txt"

&#x20;   virtualenv:   "{{ app\_dir }}/venv"



\- name: Install systemd service

&#x20; template:

&#x20;   src: flask.service.j2

&#x20;   dest: /etc/systemd/system/flask.service

&#x20;   mode: "0644"

&#x20; notify:

&#x20;   - reload systemd

&#x20;   - restart flask



\- name: Enable and start Flask

&#x20; service:

&#x20;   name: flask

&#x20;   state: started

&#x20;   enabled: yes

```

roles/flask/handlers/main.yml

```yaml

\---

\- name: reload systemd

&#x20; systemd:

&#x20;   daemon\_reload: yes



\- name: restart flask

&#x20; service:

&#x20;   name: flask

&#x20;   state: restarted

```

roles/flask/templates/flask.service.j2

Systemd-tjänst som startar Flask automatiskt:

```ini

\[Unit]

Description=Flask Application

After=network.target



\[Service]

User={{ app\_user }}

WorkingDirectory={{ app\_dir }}

Environment="PORT={{ app\_port }}"

ExecStart={{ app\_dir }}/venv/bin/gunicorn \\

&#x20;   --workers 2 \\

&#x20;   --bind 0.0.0.0:{{ app\_port }} \\

&#x20;   --access-logfile - \\

&#x20;   --error-logfile - \\

&#x20;   app:app

Restart=always

RestartSec=5

StandardOutput=journal

StandardError=journal



\[Install]

WantedBy=multi-user.target

```

roles/nginx/tasks/main.yml

```yaml

\---

\- name: Install nginx

&#x20; apt:

&#x20;   name: nginx

&#x20;   state: present

&#x20;   update\_cache: yes



\- name: Configure nginx load balancer

&#x20; template:

&#x20;   src: nginx.conf.j2

&#x20;   dest: /etc/nginx/sites-available/flask-lb

&#x20;   mode: "0644"

&#x20; notify: reload nginx



\- name: Enable site

&#x20; file:

&#x20;   src: /etc/nginx/sites-available/flask-lb

&#x20;   dest: /etc/nginx/sites-enabled/flask-lb

&#x20;   state: link

&#x20; notify: reload nginx



\- name: Remove default site

&#x20; file:

&#x20;   path: /etc/nginx/sites-enabled/default

&#x20;   state: absent

&#x20; notify: reload nginx



\- name: Start nginx

&#x20; service:

&#x20;   name: nginx

&#x20;   state: started

&#x20;   enabled: yes

```

roles/nginx/handlers/main.yml

```yaml

\---

\- name: reload nginx

&#x20; service:

&#x20;   name: nginx

&#x20;   state: reloaded

```

roles/nginx/templates/nginx.conf.j2

nginx-konfiguration med lastbalansering:

```nginx

upstream flask\_backend {

{% for host in groups\["webservers"] %}

&#x20;   server {{ host }}:{{ flask\_port }};

{% endfor %}

}



server {

&#x20;   listen 80;

&#x20;   server\_name \_;



&#x20;   location / {

&#x20;       proxy\_pass         http://flask\_backend;

&#x20;       proxy\_set\_header   Host              $host;

&#x20;       proxy\_set\_header   X-Real-IP         $remote\_addr;

&#x20;       proxy\_set\_header   X-Forwarded-For   $proxy\_add\_x\_forwarded\_for;

&#x20;   }



&#x20;   location /health {

&#x20;       proxy\_pass http://flask\_backend;

&#x20;   }

}

```

site.yml

Huvudfilen som Ansible kör:

```yaml

\---

\- name: Deploy Flask on webservers

&#x20; hosts: webservers

&#x20; become: yes

&#x20; vars\_files:

&#x20;   - vars/main.yml

&#x20; roles:

&#x20;   - flask



\- name: Configure nginx load balancer

&#x20; hosts: nginx

&#x20; become: yes

&#x20; vars\_files:

&#x20;   - vars/main.yml

&#x20; roles:

&#x20;   - nginx

```

\---

7\. Kör playbooken

```bash

\# Gå till projektmappen i WSL

cd /mnt/c/python-projekt



\# Kör Ansible-playbooken

ansible-playbook site.yml -i inventory.ini -v

```

Bra output ser ut såhär:

```

PLAY RECAP

192.168.56.10 : ok=7  changed=5  failed=0

192.168.56.11 : ok=10 changed=8  failed=0

192.168.56.12 : ok=10 changed=8  failed=0

```

> ✅ `failed=0` på alla servrar = allt fungerar!

\---

8\. Verifiera och testa

Testa lastbalansering

Öppna webbläsaren och gå till:

```

http://localhost:8080

http://localhost:8080/info

http://localhost:8080/health

```

Ladda om med `F5` – hostname ska växla mellan web1 och web2!

Testa failover

```bash

\# SSH in på web1

ssh -i /mnt/c/python-projekt/.vagrant/machines/web1/virtualbox/private\_key vagrant@192.168.56.11



\# Stoppa Flask

sudo systemctl stop flask

exit

```

Nu ska ALLA svar komma från web2 – nginx märker automatiskt att web1 är nere!

```bash

\# Starta web1 igen

ssh -i /mnt/c/python-projekt/.vagrant/machines/web1/virtualbox/private\_key vagrant@192.168.56.11

sudo systemctl start flask

exit

```

Lastbalansering återupptas automatiskt! ✅

\---

Sammanfattning – snabbreferens

```bash

\# Starta VMs

vagrant up



\# Kolla status

vagrant status



\# Testa Ansible-anslutning

ansible all -i inventory.ini -m ping



\# Kör playbooken

ansible-playbook site.yml -i inventory.ini -v



\# Testa i webbläsaren

http://localhost:8080

http://localhost:8080/info

http://localhost:8080/health

```

\---

Del 5 klar ✅ – Hela kursen klar! 🎓

