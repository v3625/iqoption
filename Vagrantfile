Vagrant.configure("2") do |config| 
  config.vm.define :host1 do |host1| 
    host1.vm.box = "ubuntu/xenial64" 
    host1.vm.hostname = "host1"
    host1.vm.network :forwarded_port, guest: 22, host: 22222
    host1.vm.network :forwarded_port, guest: 9000, host: 9001
    host1.vm.network :forwarded_port, guest: 80, host: 8001
    host1.vm.network :private_network, ip: "192.168.10.1"
    host1.vm.provider :virtualbox do |vb| 
      vb.customize ["modifyvm", :id, "--memory", "1024"] 
    end 
  end
  config.vm.define :host2 do |host2| 
    host2.vm.box = "ubuntu/xenial64" 
    host2.vm.hostname = "host2"
    host2.vm.network :forwarded_port, guest: 9000, host: 9002
    host2.vm.network :forwarded_port, guest: 80, host: 8002
    host2.vm.network :private_network, ip: "192.168.10.2"
    host2.vm.provider :virtualbox do |vb| 
      vb.customize ["modifyvm", :id, "--memory", "1024"] 
    end 
  end
  config.vm.define :host3 do |host3| 
    host3.vm.box = "ubuntu/xenial64" 
    host3.vm.hostname = "host3"
    host3.vm.network :forwarded_port, guest: 9000, host: 9003
    host3.vm.network :forwarded_port, guest: 80, host: 8003
    host3.vm.network :private_network, ip: "192.168.10.3"
    host3.vm.provider :virtualbox do |vb| 
      vb.customize ["modifyvm", :id, "--memory", "1024"] 
    end 
  end
  config.vm.define :host4 do |host4| 
    host4.vm.box = "ubuntu/xenial64" 
    host4.vm.hostname = "host4"
    host4.vm.network :forwarded_port, guest: 9000, host: 9004
    host4.vm.network :forwarded_port, guest: 80, host: 8004
    host4.vm.network :private_network, ip: "192.168.10.4"
    host4.vm.provider :virtualbox do |vb| 
      vb.customize ["modifyvm", :id, "--memory", "1024"] 
    end 
  end
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end
