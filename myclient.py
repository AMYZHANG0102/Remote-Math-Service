import socket

client = socket.socket() # Default values: AF_INET, SOCK_STREAM

host = "socketserver" # The hostname or IP address of the server
port = 9999

client.connect((host, port))

print("Welcome to the Remote Math Service!")
print("You can perform the following operations: add, sub, mul, div, mod, sqrt")
print("Note: To exit, type 'exit' or send an empty request.")

while True:
    request = input("Enter your math operation (e.g., 'add 5 3'): ")
    
    if (request.strip().lower() == "exit" or not request.strip()):
        client.send(request.encode())  # let server know client is done
        print("Disconnecting from server...")
        break
    
    try:
        client.send(request.encode()) # Send the request to the server as bytes
        response = client.recv(1024).decode() # Receive the response and decode the bytes to string
        print("Server response:", response)
        
    except Exception as e:
        print(f"Error communicating with server: {e}")
        break

client.close()