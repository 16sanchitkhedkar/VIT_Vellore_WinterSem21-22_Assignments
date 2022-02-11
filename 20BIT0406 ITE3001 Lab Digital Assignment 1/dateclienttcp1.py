import socket
host=socket.gethostname()
port=12374
s= socket.socket()
s.connect((host,port))
print (s.recv(1024).decode('utf-8'))
s.close()