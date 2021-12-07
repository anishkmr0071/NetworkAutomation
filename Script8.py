#Create a python script to connect to a cisco box and push "config" changes via external notepad. p.s: each device has its own config file. 
# Taking backups of multiple commands(show commands) for each IP, and create different files for each ip and store the outputs of show commands to their respective files
#Methods Used : open(), with open(), open modes, srtip()
	
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
	    multiple_commands = ["sh run", "sh ip int brief", "sh clock", "sh ip route"]
	    path_1 = r"C:\\Users\\anish\\PycharmProjects\\pythonProject1\\another folder\\backup_"
	
	    #openfile = open(path_1 + i + "_" +  host + ".txt", "w")
	    #openfile.write(output_1)
	    #openfile.close()
	
	    #above commented open() or with open(), using only open() will not close the file by itself, so we need to put ".close()"
	
	    with open(path_1 + i + "_" + host + ".txt", mode = "w") as openfile:
	        for c in multiple_commands:
	            output_1 = ssh_1.send_command(c)
	            openfile.write("#"*50 + c + "#" *50 +"\n")
	            openfile.write(output_1 + "\n")
	
    print(ssh_1)
