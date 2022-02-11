import socket
import random
import pickle
s=socket.socket()
host=socket.gethostname()
port=12374
s.bind((host,port))
s.listen(5)
print ('server is running: '),host,port
while True:
    c,a=s.accept()
    difference = 10**20
    propTen=random.randint(5000, 6000)
    print (b'Got connection from', a)
    k = pickle.loads(c.recv(1024))
    for i,j in k.items():
        if(difference>=abs(j-propTen)):
            difference = abs(j-propTen)
            closest = i
    c.send(closest.encode())
    c.close() 