# Methods used: import datetime, datetime.now(), import logging, send_config_from_file, With open(), find_prompt(), 
#task1, take backup with show commands, push the config file then take the post backup or post configuration show commands
#Datetime() timestamp, pre and post backup collection, Library Logging Debug [SCRIPT], send_config_from_file

from netmiko import ConnectHandler
from _datetime import datetime
import logging
logging.basicConfig(filename="today.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")
ip_list = ['192.168.30.159', '192.168.30.160']

for i in ip_list:
    device_info = {
        'device_type': 'cisco_ios',
        'ip': i,
        'username': input("enter the username:"),
        'password': input("enter the password:"),
        'secret': 'cisco'
    }
    
    ssh_1 = ConnectHandler(**device_info)
    current_time = datetime.now()
    time_1 = str(current_time.year) + "-" + str(current_time.month) + "-" + str(current_time.day)
    ssh_1.enable()
    host = ssh_1.find_prompt().rstrip("#")
    multiple_commands = ["sh run | sec ospf", "sh ip int brief", "sh clock", "logging host", "sh ip ospf neigh"]
    path_1 = r"C:\\Users\\anish\\PycharmProjects\\pythonProject1\\another folder\\backup_"

    print(time_1)
    with open(path_1 + host + "_" + i + "_" + time_1 + ".txt", mode = "w") as openfile:
        for c in multiple_commands:
            output_1 = ssh_1.send_command(c)
            openfile.write("#" * 50 + c + "#" * 50 + "\n")
            openfile.write(output_1 + "\n")
            
    #push_config_file
    device_config_file = input("enter the file to be pushed:" + host)
    push_to_device = ssh_1.send_config_from_file(device_config_file)
    print(push_to_device)
    
    #post Config
    with open(path_1 + host + "_" + i + "_" + time_1 + ".txt", mode="a") as openfile:    

    # or to write it in a new file:  with open(path_1 + host + "_" + i + "_" + time_1 + ".txt", mode="w") as openfile:
     for c in multiple_commands:
         output_1 = ssh_1.send_command(c)
         openfile.write("#" * 50 + c + "#" * 50 + "\n")
         openfile.write(output_1 + "\n")
