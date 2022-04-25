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
    total=2**(mask)
    subnetAmt=total/8
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
    ipBegin1=str(int(ipBegin[0:8], 2))
    ipBegin2=str(int(ipBegin[8:16], 2))
    ipBegin3=str(int(ipBegin[16:24], 2))
    ipBegin4=str(int(ipBegin[24:], 2))
    ipBegin=ipBegin1+"."+ipBegin2+"."+ipBegin3+"."+ipBegin4
    Beginaddr="Beginning Address is: "+ipBegin
    ipLast=ipBin [:-mask]
    for x in range(mask):
        ipLast=ipLast+"1"
    print(ipLast)
    ipLast1=str(int(ipLast[0:8], 2))
    ipLast2=str(int(ipLast[8:16], 2))
    ipLast3=str(int(ipLast[16:24], 2))
    ipLast4=str(int(ipLast[24:], 2))
    ipLast=ipLast1+"."+ipLast2+"."+ipLast3+"."+ipLast4
    Lastaddr="Last Address is: "+ipLast
    subnet1beginaddr=ipBegin4
    subnet1endaddr=ip4+31
    subnet2beginaddr=subnet1endaddr+1
    subnet2endaddr=subnet2beginaddr+31
    subnet3beginaddr=subnet2endaddr+1
    subnet3endaddr=subnet3beginaddr+31
    subnet4beginaddr=subnet3endaddr+1
    subnet4endaddr=subnet4beginaddr+31
    subnet5beginaddr=subnet4endaddr+1
    subnet5endaddr=subnet5beginaddr+31
    subnet6beginaddr=subnet5endaddr+1
    subnet6endaddr=subnet6beginaddr+31
    subnet7beginaddr=subnet6endaddr+1
    subnet7endaddr=subnet7beginaddr+31
    subnet8beginaddr=subnet7endaddr+1
    subnet8endaddr=subnet8beginaddr+31
    subnet1="Subnet 1-"+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet1beginaddr)+" - "+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet1endaddr)+"\n"
    subnet2="Subnet 2-"+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet2beginaddr)+" - "+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet2endaddr)+"\n"
    subnet3="Subnet 3-"+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet3beginaddr)+" - "+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet3endaddr)+"\n"
    subnet4="Subnet 4-"+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet4beginaddr)+" - "+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet4endaddr)+"\n"
    subnet5="Subnet 5-"+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet5beginaddr)+" - "+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet5endaddr)+"\n"
    subnet6="Subnet 6-"+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet6beginaddr)+" - "+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet6endaddr)+"\n"
    subnet7="Subnet 7-"+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet7beginaddr)+" - "+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet7endaddr)+"\n"
    subnet8="Subnet 8-"+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet8beginaddr)+" - "+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(subnet8endaddr)+"\n"
    subnets=subnet1+subnet2+subnet3+subnet4+subnet5+subnet6+subnet7+subnet8
    firstLastaddr=Beginaddr+"\n"+Lastaddr
    sock.sendto(firstLastaddr.encode(),addr)
    sock.sendto(subnets.encode(),addr)
