# http://localhost:8888/www.neverssl.com
# to run: python3 ProxyServer.py
from socket import *

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
#  Fill in start.
tcpSerSock.bind(("", 8888))
tcpSerSock.listen(100)

while 1:
    # Strat receiving data from the client
    print("Ready to serve...")
    tcpCliSock, addr = tcpSerSock.accept()
    print("Received a connection from:", addr)
    message = tcpCliSock.recv(1024)
    print(message)

    # Extract the filename from the given message
    print(message.split()[1])
    filename = message.decode().split()[1].partition("/")[2]
    fileExist = "false"
    filetouse = "/" + filename
    try:
        # Check whether the file exists in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        print("file exists", filetouse)

        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send(b"HTTP/1.0 200 OK\r\n")
        tcpCliSock.send(b"Content-Type:text/html\r\n")

        # Fill in start.
        for i in range(0, len(outputdata)):
            print(outputdata[i])
            tcpCliSock.send(outputdata[i].encode())
        # Fill in end.

        print("Read from cache")
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace(
                "www.", "", 1
            )  # this replace action may not be needed
            print(hostn)
            try:
                # Connect to the socket to port (80 or whatever it is)
                # Fill in start.
                c.connect((hostn, 80))
                # Fill in end.

                req = ("GET http://" + filename + " HTTP/1.0\r\n\r\n").encode()

                c.send(req)

                # Read the response into buffer
                output = b""
                while True:
                    data = c.recv(2048)
                    if not data:
                        break
                    output += data
                    
                # Create a new file in the cache for the requested file.
                # Also send response in buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename, "wb")
                # Fill in start.
                tmpFile.write(output)
                tcpCliSock.send(output)

                # Fill in end.
                tmpFile.close()
            except Exception as e:
                print("Illegal request", e)

            c.close()
        else:
            # HTTP response message for file not found
            # Fill in start.
            # HTTP response message for file not found
            tcpCliSock.send("HTTP/1.0 404 sendErrorErrorError\r\n")
            tcpCliSock.send("Content-Type:text/html\r\n")
            tcpCliSock.send("\r\n")

            # Fill in end.
    # Close the client and the server sockets
    tcpCliSock.close()
tcpSerSock.close()
