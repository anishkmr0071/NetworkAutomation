# Script to push the config if the configuration is missing,
# used: if, else conditions to push the config from file (used .send_config_from_file())
from netmiko import ConnectHandler
import datetime
import getpass
import logging
logging.basicConfig(filename="today.log", level= logging.DEBUG)
logger = logging.getLogger("netmiko")
ip = ["192.168.30.163", "192.168.30.164"]
for i in ip:
    device_info = {
        "device_type": "cisco_ios",
        "ip" : i,
        "username": "admin",
        "password": "cisco",
        "secret": "cisco"
    }
    ssh_session  = ConnectHandler(**device_info)
    en_session = ssh_session.enable()
    cmd_1 = ssh_session.send_command("sh run | in logging")
    print(cmd_1)
    if "23.3.3.3" in cmd_1:
        print("Logging Host is already configured")
    else:
        push_file = ssh_session.send_config_from_file(r"C:\Users\anish\PycharmProjects\pythonProject1\day8.txt")
        #print(push_file)
        #or
        #push_file = ssh_session.send_config_from_file(input("enter the file name:"))
        #or
        #push_file = ssh_session.send_config_from_file("C:\\Users\\anish\\PycharmProjects\\pythonProject1\\day8.txt")
        push_file
    print(cmd_1)
    if "23.3.3.3" in cmd_1:
        print("Successfully pushed the file")
    else:
        print("Not updated")
