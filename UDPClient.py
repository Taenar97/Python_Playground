import socket
serverName = '192.168.0.15'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MSG = input("Message? ")
MSG = MSG.encode('utf-8')
clientSocket.sendto(MSG, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage)
clientSocket.close()
