import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
print(s, host, port)
print(dir(socket))
print(f'127.0.0.1:{port}')

s.listen(5)                 # Now wait for client connection.
while True:
   # c is a connection object
   c, addr = s.accept()     # Establish connection with client.
   print(f'Got connection from {addr}')
   c.send(b'Thank you for connecting')
   c.close()  