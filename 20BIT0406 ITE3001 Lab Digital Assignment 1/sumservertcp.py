import socket
s = socket.socket()
host=socket.gethostname()
port=12374
s.bind((host,port))
s.listen(5)
print ('server is running: '),host,port
while True:
    c, add=s.accept()
    sum = 0
    print('Client connected: ',add) 
    n=c.recv(1024).decode()
    s=str(n)
    print(len(s))
    totalSum=0
    for i in range(0, len(s), 2):
	    totalSum = totalSum + int(s[i])
    c.send(str(totalSum).encode())
    c.close()