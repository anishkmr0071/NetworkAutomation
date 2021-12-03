# This is same as Script 4, but if the device list (ip address is stored in a text file) is in another folder path, then use the follwoing script:
# using: open(), split(), splitlines(), json.loads(): to read the text from a notepad.
#send_command
#Send_config_set
#input()
#open() or open(r'C:\Users\anish\doc\)
#split()
#splitlines()

from netmiko import ConnectHandler
import json

credentials = open("credentials.txt").read()
print(credentials)

js = json.loads(credentials)
print(js)
print(type(js))

Multiple_devices = open(r'C:\Users\anish.yavapuram\PycharmProjects\pythonProject1\another folder\multiple_device_list.txt').read().split(",")

for i in Multiple_devices:
    cisco_box = {
        "device_type": "cisco_ios",
        "ip": i,
        "username": js["username1"],
        "password": js['password1']
    }
    
    ssh_session = ConnectHandler(**cisco_box)
    print(ssh_session)
    print(ssh_session.find_prompt())

    sending_command_1 = ssh_session.send_command("sh running")
    print(sending_command_1)
    print(ssh_session.find_prompt())

    sending_command_2 = ssh_session.send_config_set(["do sh ip int br", "do sh clock"])
    print(sending_command_2)
