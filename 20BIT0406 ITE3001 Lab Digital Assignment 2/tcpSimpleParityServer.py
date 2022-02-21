import socket
s=socket.socket()
host=socket.gethostname()
port=12374
s.bind((host,port))
s.listen(5)
print ('server is running: '),host,port
while True:
    c,a=s.accept()
    print (b'Got connection from', a)
    stringbin=c.recv(2048).decode()
    num=stringbin.count('1')
    if(num%2==0):
        c.send(str.encode('No Error'))
    else:
        c.send(str.encode('Error'))
    c.close()

    