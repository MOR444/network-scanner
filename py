#network-scanner

#Import module
import socket
import random
import subprocess
import os

#Enter the ip you want to check
ip_address =input("Enter the target ip: ") 

#Ssh port choose
SSH_PORT = 22  

#send ping to check if the target on
def ping_host(ip_address):
    try:
        command = ['ping', '-c', '4', ip_address]        
        result = subprocess.run(command, capture_output=True, text=True)        
        print(result.stdout)

    except Exception as e:
        print(f"Error: {e}")

ping_host(ip_address)


def scan_tcp_ports(host, start_port, end_port):
    try:
        ssh_port_open = False  # Flag to track if SSH port is open
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open")
                if port == SSH_PORT:
                    print(f"Port {port} is SSH (Secure Shell) port")
                    ssh_port_open = True  # Set the flag to True if SSH port is open
            sock.close()
        return ssh_port_open  # Return the flag value
    except Exception as e:
        print(f"Error: {e}")
        return False  # Return False in case of error

    #Use module random to chak user name
    #(it will take some time to chack.)
def sample_user(user, chars, allchars):
    sample_user = ""
    while sample_user != user:
        sample_user = random.choices(allchars, k=len(user))
        print("*****" + "".join(sample_user) + "*****")

        if "".join(sample_user) == user:
            print("The name of user is: " + "".join(sample_user))
            break

    #Use module random to check user passwprd
def sample_passw(passw, chars, allchars):
    sample_passw = ""
    while sample_passw != passw:
        sample_passw = random.choices(allchars, k=len(passw))
        print("*****" + "".join(sample_passw) + "*****")

        if "".join(sample_passw) == passw:
            print("The password is: " + "".join(sample_passw))
            break


# Check if port 22 is open
if scan_tcp_ports(ip_address, 1, 1024):
    user_name = "avi"  #User name
    all_characters = "abcdefghijklmnopqrstuvwxyz"
    sample_user(user_name, len(user_name), all_characters)

    user_pass = "ai16"  #User passwd
    all_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    sample_passw(user_pass, len(user_pass), all_characters)

    print("The username and password that found are:", user_name, user_pass)

    #Change the user password
    new_pass = input("Change the password: ")
    print("Your new password is:", new_pass)
    print("Only you know the new password XD")
else:
    print("SSH port is closed") 

#Send to the user hello file :)

file_name="yaya.txt"
file_path = os.path.expanduser("~/Desktop/")  
file_full_path = os.path.join(file_path, file_name) 

if not os.path.exists(file_full_path): 
    file = open(file_full_path, "w") 
    file.write("your computer have been hack!!\n")  
    file.close()  


    print(f"File '{file_name}' created successfully at '{file_path}'")
    with open(file_full_path, "r") as file:
        file_content = file.read()
        print("File content:")
        print(file_content)

    os.system(f"less {file_full_path}") 
else:
    print(f"File '{file_name}' already exists at '{file_path}'")
