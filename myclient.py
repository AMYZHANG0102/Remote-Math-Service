import socket

client = socket.socket() # Default values: AF_INET, SOCK_STREAM

host = "socketserver" # The hostname or IP address of the server
port = 9999

client.connect((host, port))

print("Welcome to the Remote Math Service!")
print("You can perform the following operations: add, sub, mul, div, mod, sqrt")

request = input("Enter your math operation (e.g., 'add 5 3'): ")
client.send(request.encode()) # Send the request to the server as bytes

response = client.recv(1024).decode() # Receive the response and decode the bytes to string
print("Server response:", response)

client.close()