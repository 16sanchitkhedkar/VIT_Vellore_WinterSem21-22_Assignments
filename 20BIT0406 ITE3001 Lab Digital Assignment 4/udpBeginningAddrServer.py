import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:", data.decode())
    ipInfo=data.decode('utf-8').split("/")
    ip=ipInfo[0]
    mask=32-int(ipInfo[1])
    ipSplit=ip.split(".")
    ip1=int(ipSplit[0])
    ip2=int(ipSplit[1])
    ip3=int(ipSplit[2])
    ip4=int(ipSplit[3])
    ipBin1='{0:08b}'.format(ip1)
    ipBin2='{0:08b}'.format(ip2)
    ipBin3='{0:08b}'.format(ip3)
    ipBin4='{0:08b}'.format(ip4)
    ipBin=ipBin1+ipBin2+ipBin3+ipBin4
    ipBegin=ipBin [:-mask]
    for x in range(mask):
        ipBegin=ipBegin+"0"
    print(ipBegin)
    ip1=str(int(ipBegin[0:8], 2))
    ip2=str(int(ipBegin[8:16], 2))
    ip3=str(int(ipBegin[16:24], 2))
    ip4=str(int(ipBegin[24:], 2))
    ip=ip1+"."+ip2+"."+ip3+"."+ip4
    Beginaddr="Beginning Address is: "+ip
    sock.sendto(Beginaddr.encode(),addr)