import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "151.45.0.0/24"
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
print (sock.recv(1024).decode())
print (sock.recv(1024).decode())