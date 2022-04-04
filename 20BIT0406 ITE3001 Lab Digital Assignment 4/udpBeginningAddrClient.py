import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
if sock:
    while True:
        ip = str(input("Enter IP Address with mask in format xyz.xyz.xyz.xyz/n: "))
        sock.sendto(ip.encode(), (UDP_IP, UDP_PORT))
        print (sock.recv(1024).decode())
        break