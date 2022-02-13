import socket
serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while 1:
        sentence = input("Words? ")
        sentence = sentence.encode('utf-8')
        clientSocket.send(sentence)
        modifiedSentence = clientSocket.recv(1024)
        print ('from server: ', modifiedSentence)
clientSocket.close()
