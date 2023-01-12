
## this works with connectasyncserv.py (this is the server)

# holds connections in global curlist right now: a self.peers array 
# kept reseting on each new connection

import asyncio

curlist = []


class ChatServerProtocol(asyncio.Protocol):
	def __init__(self):
		#self.transport = None
		self.peers = []

	# called which new connection is established
	def connection_made(self, transport):
		self.peers.append(transport)
		global curlist
		curlist.append(transport)
		print(f'len(curlist): {len(curlist)}')
		print(f'len(self.peers ): {len(self.peers )}')
		peername = transport.get_extra_info("peername")
		print(f"Connection from {peername}")
		print(f'self.peers: {self.peers}')

	# broadcast received message to all connected peers
	def data_received(self, data):
		message = data.decode().strip()
		print(f"Received: {message}")
		print(f'peer len: {len(self.peers)}')
		for peer in curlist:
			print(f'writing to peer {peer}\ndata is: {message.encode()}')
			peer.write(message.encode())

	# drops from list of peers which connection closed
	# this currently doesnt work due to 'transport' not being available. 
	# could hack by making the message sent include an ID of the client which can 
	# be a key to curlist if it becomes a key/value pair
	# Could also ping current connections every now and check for a response
	# and if no response they are removed from the list
	def connection_lost(self, exc):
		print(f"Connection to {curlist[0]} closed")
		curlist.pop(0)


async def main():
	loop = asyncio.get_event_loop()
	server = await loop.create_server(ChatServerProtocol, "localhost", 8274)
	await server.serve_forever()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
