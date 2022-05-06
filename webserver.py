from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM) #create a socket
    try:
        serversocket.bind(('localhost', 9000)) #opening to recieve requests on port 9000
        serversocket.listen(5) #listening to incoming requests, operating system can queue 4 incoming requests
        while(1):
            (clientsocket, address) = serversocket.accept() #make sure the request is received

            rd = clientsocket.recv(5000).decode() #we decode utf-8 to unicode
            pieces = rd.split("\n")
            if(len(pieces) > 0) : print(pieces[0]) #print url

            #we send data to browser
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>hello world</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n");
    except Exception as exc:
        print("Error:\n");
        print(exc)

    serversocket.close()

print('Access http://localhost:9000')
createServer()
