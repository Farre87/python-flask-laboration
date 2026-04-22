NGINX_IP = "192.168.56.10"
WEB1_IP  = "192.168.56.11"
WEB2_IP  = "192.168.56.12"
DB_IP    = "192.168.56.13"

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  config.vm.define "nginx" do |n|
    n.vm.hostname = "nginx"
    n.vm.network "private_network", ip: NGINX_IP
    n.vm.network "forwarded_port", guest: 80, host: 8080
    n.vm.provider "virtualbox" do |vb|
      vb.memory = 512; vb.cpus = 1
    end
  end

  config.vm.define "web1" do |w|
    w.vm.hostname = "web1"
    w.vm.network "private_network", ip: WEB1_IP
    w.vm.provider "virtualbox" do |vb|
      vb.memory = 1024; vb.cpus = 1
    end
  end

  config.vm.define "web2" do |w|
    w.vm.hostname = "web2"
    w.vm.network "private_network", ip: WEB2_IP
    w.vm.provider "virtualbox" do |vb|
      vb.memory = 512; vb.cpus = 1
    end
  end

  config.vm.define "db" do |d|
    d.vm.hostname = "db"
    d.vm.network "private_network", ip: DB_IP
    d.vm.provider "virtualbox" do |vb|
      vb.memory = 512; vb.cpus = 1
    end
  end
end