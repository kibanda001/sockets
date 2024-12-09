import socket
server_ip = "IP"
server_port = 8089
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))
request = input("Hello World")
client.send(request)
response = client.recv(4096)
print(response)
