import socketserver
import time
import threading        # to count number of threads 
import asyncio

connections = {}
con_counter = 0


## Making do_loops() which runs first() then second() in order, doing it asynchronously with 10
# nonblocking calls
async def first():
    await asyncio.sleep(1)
    return "1"

async def second():
    await asyncio.sleep(1)
    return "2"

async def do_loops():
    async def one_iteration():
        result = await first()
        print(result)
        result2 = await second()
        print(result2)
    coros = [one_iteration() for _ in range(10)]
    await asyncio.gather(*coros)


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        global con_counter
        global connections


        print('loop starting')
        loop = asyncio.new_event_loop()        # make new event loop in this thread
        loop.run_until_complete(do_loops())
        print('loop ended')

        print(f'threads: {threading.activeCount() - 1}')

        id_this_con = con_counter
        con_counter += 1
        connections[id_this_con] = self.request
        print(f'self.connections len: {len(connections)}')
        print(f'connections: {connections}')
        self.data = self.request.recv(1024).strip()
        print('starting to wait')
        time.sleep(5)
        print(f"Received data from {self.client_address[0]}: {self.data.decode()}")
        self.request.sendall(self.data)
        print('dropping connection on close')
        del connections[id_this_con]
        print(f'self.connections len on close: {len(connections)}')

class MyTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    server = MyTCPServer(("localhost", 3942), MyTCPHandler)
    server.serve_forever()