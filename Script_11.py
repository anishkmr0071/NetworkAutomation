#Manually generating 0 to 50 ethernet interfaces and check if the interfaces are up or down and provide no shut if it is down.

from netmiko import ConnectHandler
import datetime
import getpass
import logging

logging.basicConfig(filename="today.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")
#ip = ["192.168.30.163", "192.168.30.164"]
ip = ["192.168.30.163"]
for i in ip:
    device_info = {
        "device_type": "cisco_ios",
        "ip": i,
        "username": "admin",
        "password": "cisco",
        "secret": "cisco"
    }
    ssh_session = ConnectHandler(**device_info)
    en_session = ssh_session.enable()
    cmd_1 = ssh_session.send_command("sh ip int br | in administratively down")
    print(cmd_1)
    print("#" * 100)
#abc = range(0,50)
#print(abc)

#Manually generating 0 to 50 ethernet interfaces and
string_1 = []
for x in range(50+1):
    string_1.append(str(x))
print(string_1)



for p in string_1:
    li = "Ethernet1/" + p
    print(li)
    #ci = "interface" + li
    #print(ci)
    x = ssh_session.send_config_set("do sh ip int " + li)
    print(x)
    if "administratively down, line protocol is down" in x:
        ssh_session.send_config_set(["int " + li, "no shut"])
    else:
        print("it is up")


'''  with open("Day8.txt", mode="w") as output_sh_ip:
        output_sh_ip.write(cmd_1)
        print(output_sh_ip)
'''


'''
    if "23.3.3.3" in cmd_1:
        print("Logging Host is already configured")
    else:
        #push_file = ssh_session.send_config_from_file(r"C:\\Users\\anish.yavapuram\\PycharmProjects\\pythonProject1\\day8.txt")
        #print(push_file)
        #or
        #push_file = ssh_session.send_config_from_file(input("enter the file name:"))
        #or
        #push_file = ssh_session.send_config_from_file("C:\\Users\\anish.yavapuram\\PycharmProjects\\pythonProject1\\day8.txt")
        push_file
    print(cmd_1)
    if "23.3.3.3" in cmd_1:
        print("Successfully pushed the file")
    else:
        print("Not updated")
