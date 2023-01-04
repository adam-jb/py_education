# going to 127.0.0.1:8899 will activate the protocol
import asyncio

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print('connection made')
        # do more things now

    def data_received(self, data):
        self.transport.write(data)
        print('data received from client')
        # do more things now

loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServerProtocol, '127.0.0.1', 8899)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
