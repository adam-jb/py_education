
# this works with async_server_multicomms.py (this is the client)

import asyncio
import random
import time

class ChatClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print("Data sent: {!r}".format(self.message))

    def data_received(self, data):
        print("Data received: {!r}".format(data.decode()))

    def connection_lost(self, exc):
        print("The server closed the connection")
        print("Stop the event loop")
        self.loop.stop()

async def main():
    message = f"Hello World! {random.random()}"
    loop = asyncio.get_event_loop()
    coro = loop.create_connection(lambda: ChatClientProtocol(message, loop),
                              "localhost", 8274)
    transport, protocol = await coro
    transport.write(f"Hello World! {random.random()}".encode())
    time.sleep(0.5)
    transport.write(f"Hello World! {random.random()}".encode())
    time.sleep(0.5)
    transport.write(f"Hello World! {random.random()}".encode())
    
    #transport.drain()
    #loop.run_forever()
    while True:
        user_input = input("Enter 'q' to quit or press enter to continue: ")
        if user_input == 'q':
            transport.close()
            break
        await asyncio.sleep(1)

    #time.sleep(20)
    #transport.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())