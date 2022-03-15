import socket
import os
import threading
import hashlib
from random import randint
ServerSocket = socket.socket() 
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Waitiing for a Connection..')
ServerSocket.listen(5)
HashTable = {}
Regno=[]
RegnoDict={}
randomint=randint(10000, 99999)
def threaded_client(connection):
    connection.send(str.encode('ENTER USERNAME : '))
    name = connection.recv(2048)
    connection.send(str.encode('ENTER PASSWORD : '))
    password = connection.recv(2048)
    password = password.decode()
    name = name.decode()
    password=hashlib.sha256(str.encode(password)).hexdigest() 
    if name not in HashTable:
        HashTable[name]=password
        for i in range(500):
            randomint=randint(1, 16777216)
            if randomint not in Regno: Regno.append(randomint)
        print('Registered : ',name)
        print("{:<8} {:<20}".format('USER','PASSWORD'))
        for k, v in HashTable.items():
            label, num = k,v
            print("{:<8} {:<20}".format(label, num))
        connection.send(str.encode((')Your registration is successful!!!! Your registration number is {} To proceed further enter your username and password').format(randomint)))
        print("-------------------------------------------")
        
    else:
        if(HashTable[name] == password):
            connection.send(str.encode('Start filling the Online Application')) 
            print('Connected : ',name)
    while True:
        break
    connection.close()
while True:
    Client, address = ServerSocket.accept()
    client_handler = threading.Thread(
        target=threaded_client,
        args=(Client,)  
    )
    client_handler.start()
    ThreadCount += 1
    print('Connection Request: ' + str(ThreadCount))
ServerSocket.close()