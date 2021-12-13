# This script will try to ask for credentials until the authentication is successful. 
import logging
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoAuthenticationException, SSHException
logging.basicConfig(filename="today_1.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")
import datetime
ip_add = ["192.168.30.181", "192.168.30.182"]
for i in ip_add:
    a = 1
    while a<=5:
        try:
            device_info = {
                'device_type': 'cisco_ios',
                'ip': i,
                'username': input("enter the  username: "),
                'password': input("enter the password: "),
                'secret': 'cisco'
            }

            #time.sleep(5)
            ssh_session = ConnectHandler(**device_info)
            ssh_session.enable()
            out123 = ssh_session.find_prompt()
            print(out123)

            if ">" or "#" in out123:
                print(" login is successful " + i)
                break
            else:
                pass
        except NetmikoAuthenticationException:
            print("trying again")
        except SSHException:
            print("ip: "+ i + " is not configured with SSH")
        a = a + 1
        print(a)
