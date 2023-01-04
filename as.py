# chat server
import asyncio
import socket

# AF_INET is the default address family: IP4
socketA = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socketA)
print(type(socketA))

bindAddress = ("", 9999)
socketA.bind(bindAddress)

chat_history = []


#Receive data two times.
while True:
    recvData = socketA.recvfrom(100)  # 100 is the buffersize
    chat_history.append(chat_history)
    socketA.sendto(b"Hello World", serverAddress)
    print(f'chat_history: {chat_history}')

#Close the server socket.
socketA.close()