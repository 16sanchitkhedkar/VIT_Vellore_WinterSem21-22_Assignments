import socket
UDP_IP = "127.0.0.1"
IN_PORT = 5678
file = open("asq1.txt", 'w')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))
while True:
 data, addr = sock.recvfrom(1024)
 message = data.decode()
 print('Recieved message:', message)
 file.write(message)
 file.close()
 sock.sendto("HEllo".encode(), addr)