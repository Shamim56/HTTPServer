#import socket module
from socket import *
from thread import *
import sys # In order to terminate the program
    

#Prepare a sever socket
if len(sys.argv) == 2:
      serverPort = int(sys.argv[1])  
else:
    serverPort = 6789    

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


def clientthread(connectionSocket):

    while True:
         #Establish the connection
        print('Ready to serve...')
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
            break;
        except IOError:
            #Send response message for file not found
            outputdata = open("404error.html").read()
            connectionSocket.send('\nHTTP/1.1 404 File Not Found\n\n')
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
            break;

while 1: 
    connectionSocket, addr = serverSocket.accept() 
    print("connected with" + addr[0] + ":" + str(addr[1]))
    start_new_thread(clientthread, (connectionSocket,))

#Close client socket
connectionSocket.close() 
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 
