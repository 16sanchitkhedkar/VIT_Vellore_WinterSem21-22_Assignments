import socket
from datetime import date, datetime
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
localIP     = "127.0.0.1"
localPort   = 3000 
bufferSize  = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP Server Started at port 3000 at address 127.0.0.1")
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode('utf-8')
    address = bytesAddressPair[1]
    clientInfo = message.split(' ')
    clientName = clientInfo[0] + " " + clientInfo[1]
    birthday = datetime( int(clientInfo[2]), int(clientInfo[3]), int(clientInfo[4]))
    age = calculate_age(birthday)
    clientMsg = "Client informationt: Name = {}, Birthdate: {}AGE : {} years".format(clientName, birthday, age)
    clientIP  = "Client IP Address: {}".format(address)
    print(clientMsg)
    print(clientIP)
    serverResponse = clientMsg      
    bytesToSend = str.encode(serverResponse)
    UDPServerSocket.sendto(bytesToSend, address)