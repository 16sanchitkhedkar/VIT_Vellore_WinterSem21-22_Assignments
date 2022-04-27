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
    c.send (b'Thank you for connecting')
    c.close()