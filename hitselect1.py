import select
import socket

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock1.connect(("localhost", 15346))
sock1.send(b'This is a a msg!')
sock1.close()   
 
