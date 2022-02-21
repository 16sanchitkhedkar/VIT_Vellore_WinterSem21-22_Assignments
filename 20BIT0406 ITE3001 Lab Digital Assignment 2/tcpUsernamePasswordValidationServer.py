import socket
s=socket.socket()
host=socket.gethostname()
port=12374
s.bind((host,port))
s.listen(5)
print ('server is running: '),host,port
while True:
    c,a=s.accept()
    c.send(str.encode('ENTER USERNAME : '))
    name = c.recv(2048)
    c.send(str.encode('ENTER PASSWORD : '))
    password = c.recv(2048)
    password = password.decode()
    name = name.decode()
    if(password=='1234' and name=='abcd'):
        c.send(str.encode('Connection Successful')) 
        print('Connected : ',name)
    else:
        c.send(str.encode('Login Failed'))
        print('Connection denied : ',name)
    while True:
        break
    c.close()