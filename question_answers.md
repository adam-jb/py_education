

## If you are making a 1000 node k8s cluster for NN training, what components would you use ? (Eg: training workers, database, and all the rest)

Containers which do the main training

PV and PVC and StorageClass for data storage as volumes being mounted: saving at each epoch maybe

May want a database to store training data too

Permissions for users to run jobs: Role based access control (RBAC): make a Role or ClusterRole and assign it to a user or group with a RoleBinding

Logging health of nodes and that they're being used: kubepromstack. And network speeds.

In Grafana, a mixin is a way to reuse a set of panels in multiple dashboards. 





## Bootstrap a K8s cluster together from scratch in AWS

[Based on Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)

on command console: install cfssl; cfssljson; kubectl

in GCP: make a VPC, subnets, firewall rules, public IP address, compute engine instances (for both workers and controllers)

generate ssh keys to access each compute engine instance

provision a certificate authority to generate TLS certificates; use cfssl to make .pem certificates

generate client and server certificates for:
- admin
- each kubelet worker
- kube-controller-manager
- kube-proxy
- kube-scheduler
- kubernetes API server
- service account

Copy certificates for each kubelet worker to each worker machine. Copy a load of other certificates to the controller machines

Generate kubeconfig files for each worker, kube-proxy, kube-controller-manager, kube-scheduler, admin. Then distribute to workers and controllers as appropriate. 

Create an encryption key and config file: distribute this to all controllers

For each controller: ssh into it, download and install etcd binaries, configure the server, create the etcd.service systemd unit file, start the etcd Server. When all are done list cluster members to verify etcd bootstrap.

Each each controller: ssh into it, download and install the Kubernetes Controller binaries, configure the API server, create kube-apiserver.service systemd unit file, kube-controller-manager.service systemd unit file, create the kube-scheduler.yaml configuration file and call it in a new kube-scheduler.service systemd unit file

Start systemd controller service with systemd

install, configure and run nginx to allow http health checks

Make system:kube-apiserver-to-kubelet clusterRole, bind it to user 'kubernetes' by creating a ClusterRoleBinding

GCP: Provision what is needed for a Network Load Balancer (this doesn't include a GCP managed load balancer service). It does include separate gcloud commands to set target-pools, forwarding-rules, firewall-rules, http-health-checks 

For each worker node: ssh into it, Download and Install Worker Binaries, Retrieve the Pod CIDR range for the current compute instance, create conf file for a 'bridge' network, create a loopback network configuration file, create containerd config file and service, make kubelet-config.yaml and reference it with kubelet.service, make kube-proxy-config.yaml and reference it when you also create kube-proxy.service. Start these services with systemctl

Generate a kubeconfig file which allows connection to cluster via kubectl as admin user

Create new routes between workers so that all pods can talk to each other

Deploy the coredns cluster add-on using off-the-shelf yaml for coredns



Q: what is a 'bridge network' in kubernetes?
A:  (from chatGPT) virtual network that connects multiple network namespaces on a single host. When a container is created in Kubernetes, it is automatically connected to a bridge network. Each container is assigned a unique IP address within the bridge network.  To allow communication between containers running on different hosts, you can use a Kubernetes feature called Services. Services allow you to expose a container to the external network and route traffic to it based on its IP address and port.

Q: why use 'loopback network configuration file' in kubernetes?
A: allow pods running on the same node to communicate with each other using the pod's IP addresses, rather than their host IP addresses.




## Use asyncio.Protocol to make an async server which can hold connections to multiple users at once, broadcasting chat text whenever anyone sends anything. 

Split over server and client scripts below. Server script is imperfect. 

Server:
```

## this works with connectasyncserv.py (this is the server)

# holds connections in global curlist right now: a self.peers array 
# kept reseting on each new connection

import asyncio

curlist = []


class ChatServerProtocol(asyncio.Protocol):
	def __init__(self):
		#self.transport = None
		#self.peers = []

	# called which new connection is established
	def connection_made(self, transport):
		global curlist                            # using instead of self.peers which resets with every new con
		curlist.append(transport)
		print(f'len(curlist): {len(curlist)}')
		peername = transport.get_extra_info("peername")
		print(f"Connection from {peername}")

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


```
Client:
```

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
    loop = asyncio.get_event_loop()
    coro = loop.create_connection(lambda: ChatClientProtocol(message, loop),
                              "localhost", 8274)
    transport, protocol = await coro
    transport.write(f"Hello World! {random.random()}".encode())

    while True:
        user_input = input("Enter 'q' to quit or press enter to continue: ")
        if user_input == 'q':
            transport.close()
            break
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


```


## Make an multithread server which multi-thread writes to a database (for logs)

The below uses ThreadPoolExecutor but only ever uses a single thread. 

Server:
```
import logging
import socketserver
from concurrent.futures import ThreadPoolExecutor
import time

class LoggingTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        message = self.request.recv(1024).strip().decode()
        logging.warning(f"Received message from {self.client_address[0]}: {message}")
        print("Number of threads: ", len(executor._threads))
        time.sleep(20)
        print("sleep done and threads now number: ", len(executor._threads))


class LoggingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def setup_logging(log_file):
    logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=log_file,
                        filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

if __name__ == "__main__":
    log_file = "server.log"
    setup_logging(log_file)
    with ThreadPoolExecutor() as executor:
        print("Number of threads:", len(executor._threads))
        server = LoggingTCPServer(("localhost", 9030), LoggingTCPHandler)
        executor.submit(server.serve_forever)
```
In the above executor.submit(server.serve_forever) submits the server.serve_forever() method to the thread pool executor. This method starts the server and runs it in a separate thread, so that it can handle multiple client connections concurrently: it only runs one thread.

The ThreadPoolExecutor class, which is used to run the server in a separate thread, creates a pool of worker threads and assigns tasks to them.

Client which writes to this:
```
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9030                # Reserve a port for your service.

data = "Hello Server!";

s.connect((host, port))
s.send(data.encode())
s.close()
```



## Make multi-thread socket connections to various external clients

Unlike the example above, the server below does create a new thread for each connection

The ThreadingMixIn class allows the server to handle multiple client connections concurrently by creating a new thread for each incoming connection

Server uses global variables as 'self' properties seem not to hold info. 
```
import socketserver
import time
import threading        # to count number of threads 

connections = {}
con_counter = 0

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        global con_counter
        global connections

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
```

This is the client which sends to the server:
```
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 3942                # Reserve a port for your service.

data = "Hello Server!";

s.connect((host, port))
s.send(data.encode())
s.close()
```

## Version of the above with lots of non-blocking calls being made from each thread the server creates

This is much like the server code in the previous section, but with asyncio.new_event_loop() and loop.run_until_complete() and such functions and asyncio doing many things at once (ie, non-blocking) for each thread

```
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
        # make new event loop in this thread as the thread doesnt have one, having just been made
        loop = asyncio.new_event_loop()        
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
```


## unittests to check the server created in the previous section is operating well

- what setUp() things will need to be created? 
- What are the likely failure modes to look for?
- good practices for unittest'ing asyncio and socketserver





































