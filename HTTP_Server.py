#import socket module
from socket import *
import sys # In order to terminate the program
    

#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 4035))
serverSocket.listen(1)


while True:
     #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    message = connectionSocket.recv(1024)
    filename = message.split()[1]
    try:
        outputdata = open(filename[1:]).read() 
         #Send one HTTP header line into socket
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n')                      
         #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        outputdata = open("404error.html").read()
        connectionSocket.send('\nHTTP/1.1 404 File Not Found\n\n')
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

#Close client socket
connectionSocket.close() 
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 
