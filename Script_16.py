#The following script use the file_transfer module (using put and get) and perform the file transfer between the network device and the host. Following 2 lines are important to do the file_transfer operation
#	1) from netmiko import file_transfer 
#	2)  backup_upload = file_transfer(ssh_login, source_file="testing.txt", dest_file="testing_uploaded_1.txt",file_system="disk0:", direction="put")



#Script SCP
from netmiko import ConnectHandler
from netmiko import file_transfer
import logging
logging.basicConfig(filename="today_11_11_2021.log",level=logging.DEBUG)
logger = logging.getLogger("netmiko")

ip_list = ['192.168.30.181', '192.168.30.182']

for ip in ip_list:
    device_info = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco'
    }
    ssh_login = ConnectHandler(**device_info)
    ssh_login.enable()
    ssh_output = ssh_login.find_prompt()
    print(ssh_output)
    commands = ssh_login.send_config_set("do dir") #"ip scp server enable")
    print(commands)

    with open("testing.txt", mode="w") as testing:
        input_1 = testing.write("ip address: 192.168.30.181 and 192.168.30.182")

    backup_upload = file_transfer(ssh_login, source_file="testing.txt", dest_file="testing_uploaded_1.txt",
                                  file_system="disk0:", direction="put")

    commands_1 = ssh_login.send_command("dir")
    print(commands_1)
