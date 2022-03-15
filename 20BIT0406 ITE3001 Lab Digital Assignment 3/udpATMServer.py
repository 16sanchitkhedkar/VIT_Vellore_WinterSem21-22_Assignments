import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))
d = dict()
while True:
    h, a = s.recvfrom(1024)
    h = h.decode()
    if h == "register":
        b, a = s.recvfrom(1024)
        b = b.decode().split("$#$")
        cno, pin, name = b[0], b[1], b[2]
        d[cno] = [pin, name, 0]
        s.sendto("registered".encode(), a)
    elif h == "add":
        b, a = s.recvfrom(1024)
        b = b.decode().split("$#$")
        cno, pin, amount = b[0], b[1], int(b[2])
        if not cno in d.keys() or d[cno][0] != pin:
            s.sendto("wrong pin".encode(), a)
        else:
            d[cno][2] += amount
            s.sendto("added balance".encode(), a)
    elif h == "withdraw":
        b, a = s.recvfrom(1024)
        b = b.decode().split("$#$")
        cno, pin, amount = b[0], b[1], int(b[2])
        if not cno in d.keys() or d[cno][0] != pin:
            s.sendto("wrong pin".encode(), a)
        elif d[cno][2] < amount:
            s.sendto("error: balance too low".encode(), a)
        else:
            d[cno][2] -= amount
            s.sendto("withdraw successful".encode(), a)
    else:
        s.sendto("unknown operation".encode(), a)