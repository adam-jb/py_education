
## Notes from book

GNS3 to emulate, configure, test and troubleshoot virtual and real networks. Network development tool.

Pexpect: for spawning child applications, controlling them, and responding to expected patterns in their output. Main commands:
- expect() - shows py will expect values to be returned
- sendline() - send command to the spawned shell
- pxssh() - for ssh connections (rather than telnet)

telnet command is a user interface to the TELNET protocol. We can use the telnet command to manage a remote machine using the command line. It's similar to the ssh command. The difference is that 

Q: difference between ssh and telnet?
A: ssh uses encryption, whereas telnet sends information in plain text.

Paramiko = Python implementation of the SSHv2 protocol. Basically a wrapper for interacting with a remote console via python. Used by Ansible when networking, eg:
```
connection.connect('172.16.1.20', username='cisco', password='cisco',
   look_for_keys=False, allow_agent=False)
stdin, stdout, stderr = connection.exec_command('show version | i V')
stdout.read()
```
The below function clear_buffer(connection) is checking if there is data ready to be received on the connection object. If there is, it is using the recv() method to receive the data and discarding it by setting the maximum buffer size using max_buffer. This effectively clears any data that may be waiting in the buffer on the connection.
```
def clear_buffer(connection):
   if connection.recv_ready():
       return connection.recv(max_buffer)
```
Can load a key to use in ssh connection:
```
key = paramiko.RSAKey.from_private_key_file('/home/echou/.ssh/id_rsa')
```
Intent-driven networking (IDN) refers to a network management approach in which network administrators define high-level business or operational goals for the network, and a network management system automatically configures the network to meet those goals. The goal of IDN is to make network configuration and management more automated, efficient, and reliable.

Intent-based networking (IBN) is a type of IDN that uses a declarative model to represent the desired state of the network. In IBN, administrators express their intent for the network in a high-level, human-readable language, and the network management system translates that intent into specific network configurations.

Process of creating data model, from wikipedia: https://en.wikipedia.org/wiki/Data_modeling

Cisco NX-API can control network rules: it's a REST endpoint - that's how you interact with it. Think cloud providers have their own things now so may be obsolete. Example of interacting with Nexus device:
```
from ncclient import manager
   conn = manager.connect(
           host='172.16.1.90',
           port=22,
           username='cisco',
           password='cisco',
           hostkey_verify=False,
           device_params={'name': 'nexus'},
           look_for_keys=False)
   for value in conn.server_capabilities:
       print(value)
   conn.close_session()
```

If you do work with Junos network, use PyEZ py module to interact with it

One advantage of ansible: No software or agent needs to be installed on the client that communicates back to the server:  Ansible uses SSH or API calls to push the required changes to the remote host. 

Ansible uses a push model to push the changes to the device: everything originates from the control machine

Ansible looks at the /etc/ansible/hosts file for hosts specified in your playbook. This is called an 'inventory' file. Or you can specify the hosts with the -i flafg

Q: what is a 'host' in Ansible?
A: a target machine. Hosts are specified in example inventory file below, with group names in [square brackets]. A host can belong to multiple groups
```
[webservers]
server1.example.com
server2.example.com
server3.example.com

[otherservers]
server1.example.com
server5.example.com
```
ansible uses the Jinja2 templating system convention of a double curly bracket {{ variable_name }}

ansible playbook is interpreted locally first and commands or configurations are pushed out later on as needed. Why? Because Ansible runs on python and can't guarantee the host will have python ready to run

network equipment can be connected via both SSH or API, depending on the platform and software release

'provider' argument in ansible: collection of arguments used to define how to connect to the network device. See example of this below

```
 ---
   - name: Configure SNMP Contact
     hosts: "nexus_by_name"
     gather_facts: false
     connection: local
		vars: 
			cli:
		         host: "{{ ansible_host }}"
		         username: "{{ username }}"
		         password: "{{ password }}"
		         transport: cli
	     tasks:
	       - name: configure snmp contact
	         nxos_snmp_contact:
	           contact: TEST_1
	           state: present
	           username: cisco123
	           password: cisco123
	           provider: "{{ cli }}"
	         register: output
```
switch = a device that connects different devices or networks together, it can forward and filter packets based on their MAC address, VLAN, IP or other header information, and the playbook is used to configure and manage the switch

ansible has if/when/then/etc flow control and conditionals, also loops (jinja syntax is used for loops)

In Ansible, the gather_facts setting is used to control whether or not Ansible gathers information about the target hosts before executing tasks on them.

Might make a template jinja file for a playbook, then can insert specific values from py script

by default, ansible looks for groups of variables to loop over in 'group_vars/all'. Looks for hosts in 'host_vars/localhost'

The below will run a playbook and allow the insertion of encrypted data:
```
ansible-playbook chapter5_10.yml --ask-vault-pass
```
The passwords used to encrypt and decrypt vault files are stored in a separate file, called the Ansible Vault password file. Can also store it as an env variable: ANSIBLE_VAULT_PASSWORD_FILE

one playbook can import another with the 'include' statement

 A role is a collection of tasks, files, templates, and variables that can be used together to perform a specific function or set of functions.

Ansible Galaxy is to ansible what Helm is to K8s

ansible py library lets you create playbook files. Good for automating creation of playbook files with python (loops, variables, etc). Example of creating a basic playbook:
```
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            x=dict(type='int', required=True),
            y=dict(type='int', required=True),
        ),
    )

    x = module.params['x']
    y = module.params['y']

    sum = x + y

    module.exit_json(changed=False, sum=sum)

if __name__ == '__main__':
    main()
```

variable-length subnet masks (VLSMs) allow for more efficient use of IP address space.

IGP (Interior Gateway Protocol) refers to a class of routing protocols that are used to distribute routing information within a single autonomous system (AS). OSPF (Open Shortest Path First) is one protocol under the umbrella of IGP

scapy is used to make your own custom packets: good for security
```
# Install and run scapy for the first time to make and send an ICMP packet:
git clone https://github.com/secdev/scapy
cd scapy/
sudo python setup.py install
sudo scapy -H
send(IP(dst="10.0.0.14")/ICMP())

# the scapy console opened with 'sudo scapy -H' is also a python console
```
tcpdump = command line packet analyser

Packet sniffing is the process of capturing all the packets flowing across a computer network. scapy.sniff() lets you do this

 The packet sniffer normal captures a copy of the data packets that are passing through so the packet continues on it's journey after being sniffed.

 Scapy is a powerful interactive packet manipulation program. It is able to forge or decode packets of a wide number of protocols, send them on the wire, capture them, match requests and replies, and much more. It can easily handle most classical tasks like scanning, tracerouting, probing, unit tests, attacks or network discovery

Can use scapy to test how resilient your system is to attacks, eg: DDoS attack by sending lots of pings at it.

can use ansible to configure access lists

routers and switches process packets at a much faster rate than servers: they do not need to see the application layer information, rather they just examine the layer 3 and layer 4 information, and decide whether the packets can be forwarded on or not. So we implement access lists at the routers and switches: it's more efficient

Gives some default rules for access control list:
- Deny RFC 3030 special-use address sources, such as 127.0.0.0/8 
- Deny RFC 1918 space, such as 10.0.0.0/8
- Deny our own space as the source IP; in this case, 10.0.0.12/30 
- Permit inbound TCP port 22 (SSH) and 80 (HTTP) to host 10.0.0.14 
- Deny everything else

Example of part of the playbook to define an access control list:
```
 tasks:
     - nxos_acl:
         name: border_inbound
         seq: 20
         action: deny
         proto: tcp
         src: 172.16.0.0/12
         dest: any
         log: enable
         state: present
         provider: "{{ cli }}"
     - nxos_acl:
         name: border_inbound
         seq: 40
         action: permit
         proto: tcp
         src: any
         dest: 10.0.0.14/32
         dest_port_op: eq
         dest_port1: 22
         state: present
         log: enable
         provider: "{{ cli }}"
```
Syslog and Uncomplicated Firewall (UFW) are both recommended for sending logs of things going on: recommends combing through the produced logs every now and then to check for breaches

SNMP = standardized protocol used to collect and manage devices. Says in practice ppl only use it to harvest info, not manage devices. Operates on UDP, with added cryptographic security

In the context of Simple Network Management Protocol (SNMP), a Management Information Base (MIB) is a database used to store information about the configuration and performance of network devices, such as routers and switches.

PySNMP to access SNMP via py. This pacakge can be used to sniff packets. Uses ASN.1: a standard and notation that describes rules and structures for representing, encoding, transmitting, and decoding data

GPT created example of using pysnmp to get access to packet:
```
# cmdgen creates SNMP commands
from pysnmp.entity.rfc3413.oneliner import cmdgen

# Create an SNMP command generator
cmd_gen = cmdgen.CommandGenerator()

# Specify the IP address and SNMP community of the network device
ip_address = '192.168.1.1'
community = 'public'

# Use the getCmd() method to create an SNMP GET request for the OID of the desired information
error_indication, error_status, error_index, var_binds = cmd_gen.getCmd(
    cmdgen.CommunityData(community),
    cmdgen.UdpTransportTarget((ip_address, 161)),
    '1.3.6.1.2.1.2.2.1.10.1'  # OID for interface 1's in octets
)

# Check for errors
if error_indication:
    print(f'Error: {error_indication}')
else:
    if error_status:
        print(f'Error: {error_status.prettyPrint()} at {error_index}')
    else:
        # Print the retrieved information
        for name, val in var_binds:
            print(f'{name.prettyPrint()} = {val.prettyPrint()}')
```
Monitoring can be pull based (where monitor sends requests to all hosts periodically) or push based (where monitor subscribes to hosts)

Can use 'struct' module to convert between Python values and C structs represented as Python bytes objects

The below uses struct module to encode multiple values of different types into a single bytestring
```
import struct

# Pack two integers and a string into a struct
packed_data = struct.pack("!ii6s", 1234, 5678, b"hello")
print(packed_data)  # b'\xd2\x04\x00\x00\x16\xae\x00\x00hello\x00'

# Unpack two integers and a string from a struct
unpacked_data = struct.unpack("!ii6s", b'\xd2\x04\x00\x00\x16\xae\x00\x00hello\x00')
print(unpacked_data)  # (1234, 5678, b'hello\x00')
```

The below makes a socket on IPv4 and UDP protocol
```
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 9995))

# retreive data 1500 bytes at a time
while True:
    buf, addr = sock.recvfrom(1500)

```
Doing calculations 'on the wire' means doing something to the raw packet data

ntopng is a web-based traffic monitoring application you can run in terminal, is able to:
- Passive monitor traffic by passively capturing network traffic
- Collect network flows (NetFlow, sFlow and IPFIX)
- Actively monitor selected network devices
- Monitor a network infrastructure via SNMP

ntop py module lets you interact with ntopng once you have it running locally

ELK stack contains Elasticsearch, Logstash, and Kibana as a full stack to ingest information with Logstash, index and analyze data with Elasticsearch, and present the graphics output via Kibana.

Logstash is a data processing pipeline tool that ingests, transforms and forwards data to a variety of destinations. It is commonly used to collect and process log data, but can also be used to process other types of data. To monitor a cluster, you can use Logstash to collect log data from all the nodes in the cluster and forward it to a centralized destination for further processing and analysis.

Flask-SQLAlchemy: a wrapper around SQLAlchemy that simplifies the process of working with databases in Flask, by providing useful defaults and convenient methods for interacting with SQLAlchemy.

Virtual Private Cloud (VPC) needs to reside entirely in one region, and each subnet needs to reside entirely in one availability zone. On the other hand, NAT Gateway is AZ-bound, so we will need to create one per AZ if we needed redundancy. 

VPC routing facts in AWS:
- each VPC has an implicit router that is responsible for routing traffic between the various subnets within the VPC, as well as between the VPC and the Internet, or other VPCs.
- Each VPC has the main routing table with the local route populated
- You can create custom-routing tables
- Each subnet can follow a custom-routing table or the default main routing table
- The route table route target can be an internet gateway, NAT gateway, VPC peers, and so on

The important differences between the security group and ACLs are as follows:
- The security group operates at the network interface level where ACL operates at the subnet level
- For a security group, we can only specify allow rules but not deny rules, whereas ACL supports both allow and deny rules
- A security group is stateful; return traffic is automatically allowed. Return traffic needs to be specifically allowed in ACL













#### KOps vs Kubespray (from the Kubespray git page) [Source](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/comparisons.md)

Kubespray runs on bare metal and most clouds, using Ansible as its substrate for provisioning and orchestration. Kops performs the provisioning and orchestration itself, and as such is less flexible in deployment platforms.

Kops, however, is more tightly integrated with the unique features of the clouds it supports so it could be a better choice if you know that you will only be using one platform for the foreseeable future.

Can use Ansible to provision cloud resources

Q: How does kubespray work?
1. Kubespray uses Ansible to provision and configure the infrastructure that will host the cluster. This includes creating virtual machines, installing necessary packages, and configuring network settings.

2. Once the infrastructure is set up, Kubespray uses Ansible to install and configure the components of a Kubernetes cluster. This includes etcd, the control-plane (API server, etcd, etc) and the worker nodes.

3. After the Kubernetes components are installed and configured, Kubespray uses Ansible to connect the components and ensure they are communicating properly.

4. Finally, Kubespray uses Ansible to validate the cluster is running and healthy, and it can be used for further management of the cluster.



#### OSI layers

Physical layer (Layer 1) is located on the network's hardware devices such as hubs, switches, and routers. includes translating bits to electricity, light, or radio signals and controlling the rates at which they are sent over the chosen medium.

Data Link Layer (Layer 2) is located on the network interface card (NIC) of each device connected to the network. breaks data to be transmitted into frames for transmission at the physical layer. It also manages connections between two different nodes, including setting up the connection, identifying and correcting any bit errors that occur at the physical layer, and terminating the connection once the session is complete.

Network Layer (Layer 3) is located on the routers that forward packets between different networks. Network-layer devices operate on packets and are responsible for routing traffic to its destination based on IP addresses 

Transport Layer (Layer 4) is located on the end devices such as PCs and servers. Manages the transmission of data between nodes, including ensuring that data arrives in the correct sequence and that any errors are corrected

Session Layer (Layer 5) is located on the end devices such as PCs and servers

Presentation Layer (Layer 6) is located on the end devices such as PCs and servers

Application Layer (Layer 7) is located on the end devices such as PCs and servers


##### Points about the layers

- Each layer is built upon the services provided by the layer below it. For example, the Data Link Layer (Layer 2) uses the Physical Layer (Layer 1) to transmit data, and the Network Layer (Layer 3) uses the services of the Data Link Layer to route data between networks.

- Each layer communicates with the layer directly above and below it. The Physical Layer (Layer 1) communicates with the Data Link Layer (Layer 2), the Data Link Layer communicates with the Network Layer (Layer 3), and so on.

- Each layer provides a specific set of services to the layer above it, and uses a specific set of services provided by the layer below it. For example, the Transport Layer (Layer 4) provides reliable end-to-end data transfer services to the Session Layer (Layer 5), and uses the services provided by the Network Layer (Layer 3) to route data.

- Each layer has a specific interface, known as a service interface, which defines the services that it provides to the layer above it, and the services that it uses from the layer below it.

- Each layer is independent of the layers above and below it. This allows for changes to be made to one layer without affecting the other layers, as long as the service interface remains the same



##### Examples of protocols used for each of the OSI layers

Layer 1 (Physical): Ethernet, Fiber Distributed Data Interface (FDDI), Serial Line Internet Protocol (SLIP)

Layer 2 (Data Link): Address Resolution Protocol (ARP), Point-to-Point Protocol (PPP), Media Access Control (MAC)

Layer 3 (Network): Internet Protocol (IP), Internet Control Message Protocol (ICMP), Routing Information Protocol (RIP)

Layer 4 (Transport): Transmission Control Protocol (TCP), User Datagram Protocol (UDP), Stream Control Transmission Protocol (SCTP)

Layer 5 (Session): Remote Procedure Call (RPC), Session Announcement Protocol (SAP)

Layer 6 (Presentation): Simple Object Access Protocol (SOAP), Extensible Markup Language (XML)

Layer 7 (Application): Hypertext Transfer Protocol (HTTP), File Transfer Protocol (FTP), Simple Mail Transfer Protocol (SMTP). REST APIs are based on HTTP so are Layer 7.










Q: what is a MAC address?
A: MAC Addresses are unique 48-bits hardware number of a computer, which is embedded into a network card (known as a Network Interface Card) during the time of manufacturing. MAC Address is also known as the Physical Address of a network device



Q: what is a MPLS network (Multiprotocol Label Switching ) ?
A: type of data-carrying technique for high-performance telecommunications networks. It is a way to forward packets of data, also called frames, based on short path labels rather than long network addresses, such as IP addresses. Has a good few uses and is suited to high-bandwidth requirements



Q: what makes a '100G backbone' in network design?
A: high-speed network infrastructure that can transmit data at a rate of 100 gigabits per secon


To achieve a 100G backbone, several key components are needed:
- High-speed Networking Devices: This includes routers, switches, and other network devices that are capable of handling 100G data rates. These devices typically have specialized hardware and software that are optimized for high-speed transmission.
- High-speed Cabling: 100G networks require specialized cabling, such as multi-mode or single-mode fiber optic cables, that are capable of transmitting data at high speeds over long distances.
- High-speed Interfaces: Network devices must have 100G interfaces, such as 100G Ethernet, that are capable of transmitting and receiving data at 100G data rates.
- High-speed Protocols: The network must use protocols that are optimized for high-speed transmission, such as MPLS (Multiprotocol Label Switching) and MPLS-TP (MPLS Transport Profile)
- Quality of Service (QoS): A 100G backbone must have the ability to prioritize different types of traffic, such as voice and video, and ensure that they are delivered with the appropriate level of performance.



Q: what can you learn from the Ansible networking examples? (https://docs.ansible.com/ansible/latest/network/user_guide/network_best_practices_2.5.html)


Q: how can ansible and kubespray be used to set up K8s clusters? (base the answer on https://github.com/kubernetes-sigs/kubespray/tree/master/contrib/terraform/aws)























