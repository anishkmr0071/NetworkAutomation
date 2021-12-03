#this is a basic script, establishes the ssh connection to the network device and checkwhether the enable mode is configured on not. Then send a command using send_command() method

from netmiko import ConnectHandler

dict123={
'ip':'192.168.30.151',
'username':'admin',
'password':'cisco',
'device_type':'cisco_ios'
}

ssh123=ConnectHandler(**dict123)      #this checks the device_type and establishes the connection
print(ssh123)
a=ssh123.find_prompt()
print("sshissuccessfulto"+a)
input_1='en'
output_1=ssh123.send_command(input_1)
print(output_1)
test=ssh123.check_enable_mode()
print(test)

#===============================================================================================================

'''
b=["showipintbr","shclock"]
for abc in b:
out123=ssh123.send_command(abc)
print("FETCHINGTHEOUTPUTFOR"+abc)
print(out123)
'''
