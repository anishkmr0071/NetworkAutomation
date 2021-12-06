'''
User Privilege:
We will check if we are going to have same rights for user with level 1 privilege and user with level 15 privilege
If we assign a user (tim) with level 1 privilege, and try to run "sh run" command, it will through us a error. 
	But if we execute "sh ip int brief", tim can run without error. 
	This is because sh run cannot run on level 1 access.
	A user with level15 access directly goes to "R01#" (privilege mode). 
	But a user with level1 access goes to "R01>" (enable mode). For user with privilege 1 to run show run,
	And To skip this error, we are going to use of enable(), if we are using enable(), then we should also mention secret password in the initial dictionary.
	Methods used: Write_channel(), find_prompt(), read_until_prompt_or_pattern("Password:"), read_until_prompt_or_pattern("pattern= Password"), read_until_prompt("Password"), read_until_pattern("pattern= Password")
	Example:
'''
 # 1) User Privilege\
from netmiko import ConnectHandler
	
devices_1 = {
	    "device_type":"cisco_ios",
	    "username":"tim",
	    "password":"cisco",
	    "ip": '192.168.30.151',
	    "secret": "cisco"
	}
	
ssh_1 = ConnectHandler(**devices_1)
##################################################
out123 = ssh_1.send_command("sh ip int br")
print(ssh_1.find_prompt())
print(out123)
####################################################
ssh_1.enable()         #it will give you error if we don't put "secret": " ", in the devices_1 dictionary
print(ssh_1.find_prompt())
####################################################
out123_1 = ssh_1.send_command("sh run")
print(out123_1)
print(ssh_1.find_prompt())
###################################################
out123_2 = ssh_1.send_command("sh privilege")
print(out123_2)

#in the above code, enable function will take the secret pass, by itself from the dictionary. 
#But if want to do it more manually. We can do it using, read_until_prompt_or_pattern() or read_until_prompt() or read_until_pattern() or write_channel() and if condition
	
  
  
  
  
'''  
#2) Using read() method
	
  from netmiko import ConnectHandler
	devices_1 = {
	    "device_type":"cisco_ios",
	    "username":"tim",
	    "password":"cisco",
	    "ip": '192.168.30.151',
	}
	
	ssh_1 = ConnectHandler(**devices_1)
	ssh_1.write_channel("enable" + "\n")
	ssh_1.read_until_prompt_or_pattern("Password:") (or) ssh_1.read_until_prompt_or_pattern("pattern= Password") (or)  ssh_1.read_until_prompt("Password") (or) ssh_1.read_until_pattern("pattern= Password")
	ssh_1.write_channel("cisco" + "\n")
	print(ssh_1.find_prompt())
	out_123_3 = ssh_1.send_command("sh run")
	print(out_123_3)
	print(ssh_1.send_command("sh privilege"))
	print(ssh_1.find_prompt())

 '''
  
  

'''  
#3) Achieved using if else condition
	
  from netmiko import ConnectHandler
	devices_1 = {
	    "device_type":"cisco_ios",
	    "username":"tim",
	    "password":"cisco",
	    "ip": '192.168.30.151',  
	}
	ssh_1 = ConnectHandler(**devices_1)
	
	# if you want to blindly insert the password in the next line, then comment the above lines that has, read_until_prompt_or_pattern("password")
	# just put the password using the write_channel in the next line, example: like the following.
	#ssh_1.write_channel("cisco" + "\n")
	# but if you want to put the password only when it says"password", then use the function: read_until_prompt_or_pattern("password")
	
	if "Password" in vendor1:
	    ssh_1.write_channel("cisco" + "\n")
	    print(ssh_1.find_prompt())
	
	    out_123_3 = ssh_1.send_command("sh run")
	    print(out_123_3)
	
	    print(ssh_1.send_command("sh privilege"))
	    print(ssh_1.find_prompt())
	else:
	    pass
	
'''
  
'''	
Enable function limitation (Enable()):
	# For privileges betweeen 2-14, the user will enter directly to #(privilege mode), instead of going from enable to privilige.
	# but for user with privilege 1, the user will enter to enable and then it will go to privilege mode
	# when a user with priv 1, uses enable function to get the output, then for the second time when the user with 2-14,
	# tries to use the enable function, it will not work
'''
