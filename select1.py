import select
import socket

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock1.bind(("localhost", 15346))
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.bind(("localhost", 8081))

# Wait for data to be available on either socket for up to 1 second
ready, _, _ = select.select([sock1, sock2], [], [], 1)
print(f'ready: {ready}')
if ready:
    print('starting loop')
    while True:
        # Check which sockets have data available
        if sock1 in ready:
            data1 = sock1.recv(1024)
            print(f'data1 in sock1: {data1}')
            break
            # Do something with the data from sock1
        if sock2 in ready:
            data2 = sock2.recv(1024)
            # Do something with the data from sock2
            print(f'data2 in sock2: {data2}')
            break
print('done!')