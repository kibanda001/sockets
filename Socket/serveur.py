import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bind_ip ="0.0.0.0"
bind_port = 8089

server.bind((bind_ip, bind_port))
server.listen(5)
print("[+] ... Listen on address %s and Port %d" %(bind_ip, bind_port))
(client, (ip, port)) = server.accept()
print("Client IP Address : %s" %ip)
print("Client remote Port %d" %port)

data = "Hello"
response = "Thanks for contact Me"
while len(data):
    data = client.recv(2048)
    print("Client sent %s" % data)
    client.send(response)
print("Closing the connections")
client.close()
print("Server Closing")
server.close()