import asyncio
import socket

class ChatServer:
    def __init__(self):
        self.clients = []

    async def broadcast(self, message):
        for client in self.clients:
            await client.send(message)

    async def handle_client(self, client, addr):
        self.clients.append(client)
        try:
            while True:
                message = await client.recv()
                if not message:
                    break
                await self.broadcast(message)
        finally:
            self.clients.remove(client)
            client.close()

async def start_server():
    server = ChatServer()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)

    while True:
        client, addr = server_socket.accept()
        asyncio.create_task(server.handle_client(client, addr))

asyncio.run(start_server())