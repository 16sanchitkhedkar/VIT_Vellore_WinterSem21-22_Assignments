import socket
host=socket.gethostname()
port=12374
s= socket.socket()
s.connect((host,port))
stringbin=input('Enter binary ->')
parity=stringbin.count('1')
if(parity%2==0):
    stringbin+=str(0)
else:
    stringbin+=str(1)
s.send(str.encode(stringbin))
print(s.recv(2048).decode())
s.close()