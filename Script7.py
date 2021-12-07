	#1) Take Backup, fetch the output of sh run and store it locally
	#Methods Used : open(), with open(), open modes, 
	
	
	from netmiko import ConnectHandler
	import getpass
	from datetime import datetime
	ip_list = ['192.168.30.155', '192.168.30.156']
	for i in ip_list:
	    device_info = {
	        'device_type': 'cisco_ios',
	        'ip': i,
	        'username': input("enter the username:"),
	        'password': input("enter the password:"),
	        'secret': 'cisco'
	    }
	
	    ssh_1 = ConnectHandler(**device_info)
	    ssh_1.enable()
	    prompt = ssh_1.find_prompt()
	    host = ssh_1.find_prompt().rstrip("#")
	    output_1 = ssh_1.send_command("sh run")
	    path_1 = r"C:\\Users\\anish\\PycharmProjects\\pythonProject1\\another folder\\backup_"
	
	    #openfile = open(path_1 + i + "_" +  host + ".txt", "w")
	    #openfile.write(output_1)
	    #openfile.close()
	
	    #above commented open() or with open(), using only open() will not close the file by itself, so we need to put ".close()"
      #but if we use withopen(), it will close the file byitself after finishing the task.
	
	    with open(path_1 + i + "_" + host + ".txt", mode = "w") as openfile:
	        openfile.write(output_1)
	
    print(ssh_1)
