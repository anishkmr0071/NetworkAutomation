# using: for loop for multiple devices; send_config_set to pass multiple commands; used input to take credentials

from netmiko import ConnectHandler
ip_list = ["192.168.30.151", "192.168.30.152"]
for i in ip_list:
    
    cisco_box = {
        "device_type": "cisco_ios",
        "ip": i,
        "username": input("enter the username:"),
        "password": input("enter the password:")
    }
    
    ssh_session = ConnectHandler(**cisco_box)

    print(ssh_session)
    print(ssh_session.find_prompt())

    sending_command_1 = ssh_session.send_command("sh running")

    print(sending_command_1)
    print(ssh_session.find_prompt())

    sending_command_2 = ssh_session.send_config_set(["do sh ip int br", "do sh clock"])
    print(sending_command_2)
