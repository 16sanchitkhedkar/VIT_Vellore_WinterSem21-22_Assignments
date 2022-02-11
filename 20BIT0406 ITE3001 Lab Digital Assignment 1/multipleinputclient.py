import socket
import pickle
host=socket.gethostname()
port=12374
s= socket.socket()
s.connect((host,port))
userList={}
for i in range(5):
    userList["User " + str(i+1)] = int(input("Tender for User "+str(i+1)+":"))
s.send(pickle.dumps(userList))
print('\nCongratulations!!!' + s.recv(1024).decode() + ' got the Tender')