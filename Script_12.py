#automating to display list of interface and check if they are up of down. if up, pass, else, give no shut
#To enable getpass() to work on the pycharm, go to run -> edit configuration -> check the box "emulate terminal in output console"
from netmiko import ConnectHandler
import datetime
from getpass import getpass
import logging

logging.basicConfig(filename="today.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")
ip = ["192.168.30.163", "192.168.30.164"]
#ip = ["192.168.30.163"]
for i in ip:
    device_info = {
        "device_type": "cisco_ios",
        "ip": i,
        "username": input("enter the username: "),
        "password": getpass(),
        #or
        #password: getpass(prompt= str("Password")),
        "secret": "cisco"
    }
    ssh_session = ConnectHandler(**device_info)
    en_session = ssh_session.enable()
    cmd_1 = ssh_session.send_command("sh run | in interface")
    print("#" * 100)
    print("sh run | in interface, output of : " + i + "\n")
    print(cmd_1)
    print("#" * 100)

#writing the list of interfaces to a file
    with open("day8.txt", mode="w") as output_sh_run_in:
        output_sh_run_in.write(cmd_1)

# opening the file to read it and split them
    k = open("day8.txt", "r")
    l = k.read().splitlines()
    print(" l output, converted above output to list format using splitlines() function: " + "\n")
    print(l)

#converting "sh run | in interface" command output to select only interface names from the list.
    interfaces_list1 = []
    print("#" * 100)
    print("spliting the l and just displaying the interfaces:" + "\n")
    for word in l:
        strip_line = word.split().pop(1)    #word.split() will take each element from l, and split them into a string and put them in a list.
        print(strip_line)
        interfaces_list1.append(strip_line)

    print("#" * 100)
    print("List of Interfaces: " +"\n")
    print(interfaces_list1)
    print("#" * 100 + "\n")

    for interface in interfaces_list1:
        check_up_or_down = ssh_session.send_command("sh interface " + interface)
        if interface + " is up, line protocol is up" in check_up_or_down:
            print("No shut is not required for " + interface)
        elif interface + " is administratively down, line protocol is down" in check_up_or_down:
            push_no_shut = ssh_session.send_config_set(["interface " + interface, "no shut"])
            print(push_no_shut)
        else:
            pass

#post interface
    print("#" * 100)
    print("Post Sh Command output: " +"\n")
    print(ssh_session.send_command("sh ip int br"))
