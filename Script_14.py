#Using try and except method to ignore the errors;
#This script will try the lines under try, and ignore when it hit with any exception. Used "netmiko.sshexception"
#from netmiko.ssh_exception import SSHException, NetMikoAuthenticationException, NetMikoTimeoutException

from netmiko import ConnectHandler
from netmiko.ssh_exception import SSHException, NetMikoAuthenticationException, NetMikoTimeoutException
ip_add = ["192.168.30.181", "192.168.30.182"]
#multipledevice123 = open("iplist.txt").read().splitlines()
for ip in ip_add:
    device_info = {
        "device_type": "cisco_ios",
        "ip": ip,
        "username": "admin",
        "password": "cisco",
        "secret": "cisco"
    }
    try:
        ssh_login = ConnectHandler(**device_info)
        ssh_login.enable()
        output_1 = ssh_login.find_prompt()
        print(output_1)
    except SSHException:
        print("SSH not configured")
    except NetMikoAuthenticationException:
        print("Credentials Mismatched")
    except NetMikoTimeoutException:
        print("SSH Timeout")
