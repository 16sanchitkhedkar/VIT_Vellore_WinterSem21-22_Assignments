import socket
serverAddressPort = ("127.0.0.1", 3000)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
if UDPClientSocket:
    while True:
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        year = int(input("Enter birth year: "))
        month = int(input("Enter birth month: "))
        day = int(input("Enter birth day: "))
        msgFromClient = fname + " " + lname + " " + str(year) + " " + str(month) + " " + str(day)
        bytesToSend = str.encode(msgFromClient)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "Message from Server {}".format(msgFromServer[0].decode('utf-8'))
        print(msg)
        toCont = input("Do you want to continue or enter exit to stop: ")
        if toCont.lower() == "exit":
            break