# using: open(), split(), splitlines(), json.loads(): to read the text from a notepad.

#send_command : It sends the command that we mention, we can use this command after ssh is established. This is a method in base connection. It takes only one command and applies to only privilege mode You can use for loop and send multiple commands.
#Send_config_set: It takes multiple commands using list, applies in global configuration mode and after executing the command, it will end and come back to privilege mode. 
#input(): It will take username input and password input from the user
#open() or open(r'C:\Users\anish\doc\): open(r"C:\Users\Public\Downloads\list_of_devices.txt") (Or) open("C:\\Users\\Public\\Downloads\\list_of_devices.txt")
#split(): Example: abc123 = new_list_multiple_list123.read().split("\n")
#splitlines(): Example: open("login_cred.txt").read().Splitlines()

from netmiko import ConnectHandler
import json
ip_list = ["192.168.30.151", "192.168.30.152"]
#credentials = open("credentials.txt").read().splitlines()
credentials = open("credentials.txt").read()
print(credentials)
js = json.loads(credentials)
print(js)
print(type(js))

for i in ip_list:
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
