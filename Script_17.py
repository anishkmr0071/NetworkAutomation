#this script focus on resetting the ospf neighbor connections using the "clear ip ospf" command.
#using send_command_timing() method to send the clear ip ospf process. and also it waits to a default of 1 sec to display the prompt of "clear ip ospf process".

from netmiko import ConnectHandler
import logging
logging.basicConfig(filename="today_1_31_2022.log",level=logging.DEBUG)
logger = logging.getLogger("netmiko")

ip = open("C:\\Users\\anish\\PycharmProjects\\pythonProject1\\iplist.txt")

for i in ip:
    print(i)
    device_information = {
    "device_type" : "cisco_ios",
    "ip" : i,
    "username" : "admin",
    "password" : "cisco",
    "secret" : "cisco"
    }
    ssh_login = ConnectHandler(**device_information)
    print(ssh_login.find_prompt())
    sh_ip= ssh_login.send_command("sh ip int br")
    #print(sh_ip)
    ssh_login.enable()

    # configuring ospf
    if "FastEthernet0/0 is up" in ssh_login.send_command("sh ip ospf interface"):
        print(ssh_login.send_command("sh ip ospf neighbor"))
    else:
        config_ospf = ssh_login.send_config_set(["router ospf 100", "network 192.168.30.0 0.0.0.255 area 0", "\n"])
        print(config_ospf)

    # clearing ospf process
    clear_process_1 = ssh_login.send_command_timing("clear ip ospf process")
    print(clear_process_1)
    i = 0
    while i <= 10:
        if "Reset" in clear_process_1:
            user_input = input("types Yes or No: ")
            if "yes" in user_input:
                print ("reset performed successfully")
                break
            elif "no" in user_input:
                print("user denied reset Task")
                break
            else:
                print("Wrong Input, try again")

        else:
            pass

#CHECK THE #SH IP OSPF NEIGHBOR <NEIGHBOR ID>, FOR THE UPTIME OF THE NEIGHBOR. IT WILL CHANGE Now.



