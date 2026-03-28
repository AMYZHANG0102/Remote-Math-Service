import socket

client = socket.socket()

host = socket.gethostname()
port = 9999

client.connect((host, port))
client.send("add 5 3".encode())
response = client.recv(1024).decode()
print("Server response:", response)
client.close()