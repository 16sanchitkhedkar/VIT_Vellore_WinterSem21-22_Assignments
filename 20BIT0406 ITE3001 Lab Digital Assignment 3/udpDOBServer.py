from calendar import month
import socket
from datetime import date, datetime
def calculate_year(born):
    birth_year = born.year
    current_year = date.today().year
    age_year = current_year - birth_year
    return age_year

def calculate_month(born):
    birth_month = born.month
    current_month = date.today().month
    age_month = abs(current_month-birth_month)
    return age_month

def calculate_day(born):
    birth_day = born.day
    current_day = date.today().day
    age_day = abs(current_day-birth_day)
    return age_day

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
    year = calculate_year(birthday)
    month = calculate_month(birthday)
    day = calculate_day(birthday)
    clientMsg = "{} your age is {} years {} months {} days".format(clientName, year, month, day)
    clientIP  = "Client IP Address: {}".format(address)
    print(clientMsg)
    print(clientIP)
    serverResponse = clientMsg      
    bytesToSend = str.encode(serverResponse)
    UDPServerSocket.sendto(bytesToSend, address)