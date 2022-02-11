import socket
host=socket.gethostname()
port=12374
s= socket.socket()
s.connect((host,port))
n=input("Enter a 6 digit number: ") 
s.send(n.encode()) 
print('Sum of index 0, 2, 4:',s.recv(1024).decode())