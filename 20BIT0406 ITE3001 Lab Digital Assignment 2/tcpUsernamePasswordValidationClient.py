import socket
host=socket.gethostname()
port=12374
c= socket.socket()
c.connect((host,port))
response=c.recv(2048)
name=input(response.decode())
c.send(str.encode(name))
response = c.recv(2048)
password = input(response.decode())	
c.send(str.encode(password))
response = c.recv(2048)
response = response.decode()
print(response)
c.close()