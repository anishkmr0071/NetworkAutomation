from netmiko import ConnectHandler
#user_name_1 = input('enter the username:')
#password_1 = input("enter the password:")
Devices = ['192.168.30.151', '192.168.30.152']
for i in Devices:
    dict_1 = {
        "device_type": "cisco_ios",
        "ip": i,
        "username": input('enter the username:'),
        "password": input("enter the password:"),

    }
    ssh_1 = ConnectHandler(**dict_1)
    print(ssh_1)
    Sh_commands = ssh_1.send_command("sh ip int brief | include up")      #send_command can only send one command at a time,
                                                                        # but send-config_set can send multiple commands
    #print(ssh_1.find_prompt())
    print(Sh_commands)
    print("************************************************")
print("#" * 100)
config_commands = ssh_1.send_config_set(["do sh ip int brief", "logging host 192.168.30.151", "do sh ip int brief | include up"])
print(config_commands)
