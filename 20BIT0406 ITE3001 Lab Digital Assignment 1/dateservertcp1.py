import socket
from datetime import datetime
s=socket.socket()
host=socket.gethostname()
port=12374
s.bind((host,port))
s.listen(5)
print ('server is running: '),host,port
while True:
    c,a=s.accept()
    print (b'Got connection from', a)
    now=datetime.now()
    currentTime = now.strftime("%d/%m/%Y")
    c.send (currentTime.encode('utf-8'))
    c.close()