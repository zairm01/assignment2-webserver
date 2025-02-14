from socket import *
import sys  # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)  
    serverSocket.bind(("", port))  
    serverSocket.listen(1)  

    while True:
        # Establish the connection
        print("Ready to serve...")
        connectionSocket, addr = serverSocket.accept()  
        
        try:
            message = connectionSocket.recv(1024).decode()  
            filename = message.split()[1]  

            
            f = open(filename[1:], "rb")  
            
           
            outputdata = b"HTTP/1.1 200 OK\r\n"
            outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
            outputdata += b"Server: MySimpleServer\r\n"
            outputdata += b"Connection: close\r\n\r\n"
            
            for i in f:  
                outputdata += i 
           
            
            connectionSocket.send(outputdata)
          
            
            connectionSocket.close()  
            f.close()
        
        except Exception as e:
            
            error_response = b"HTTP/1.1 404 Not Found\r\n"
            error_response += b"Content-Type: text/html; charset=UTF-8\r\n"
            error_response += b"Server: MySimpleServer\r\n"
            error_response += b"Connection: close\r\n\r\n"
            error_response += b"<html><body><h1>404 Not Found</h1></body></html>"
            connectionSocket.send(error_response)
          
            
            connectionSocket.close()
          

if __name__ == "__main__":
    webServer(13331)
