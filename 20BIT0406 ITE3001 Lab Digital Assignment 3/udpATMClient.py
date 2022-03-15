import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
type = input("register, add or withdraw: ")
s.sendto(type.encode(), (UDP_IP, UDP_PORT))
if type == "register":
    card = input("Enter card number: ")
    pin = input("Enter the pin: ")
    name = input("Enter your name: ")
    s.sendto((card + "$#$" + pin + "$#$" + name).encode(), (UDP_IP, UDP_PORT))
    print(s.recvfrom(1024)[0].decode())
elif type == "add":
    card = input("Enter card number: ")
    pin = input("Enter the pin: ")
    bal = input("Enter balance to add: ")
    s.sendto((card + "$#$" + pin + "$#$" + bal).encode(), (UDP_IP, UDP_PORT))
    print(s.recvfrom(1024)[0].decode())
elif type == "withdraw":
    card = input("Enter card number: ")
    pin = input("Enter the pin: ")
    bal = input("Enter balance to withdraw: ")
    s.sendto((card + "$#$" + pin + "$#$" + bal).encode(), (UDP_IP, UDP_PORT))
    print(s.recvfrom(1024)[0].decode())
else:
    print(s.recvfrom(1024)[0].decode())