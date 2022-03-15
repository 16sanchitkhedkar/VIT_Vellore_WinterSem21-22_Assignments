import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5678
file = open("asq1.txt", 'r')
lines = file.readlines()
message = "Digital Communications and computer Network"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in lines:
message = i
sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
print(sock.recv(1024).decode())