
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 3942                # Reserve a port for your service.

data = "Hello Server!";

s.connect((host, port))
s.send(data.encode())
s.close()


 

