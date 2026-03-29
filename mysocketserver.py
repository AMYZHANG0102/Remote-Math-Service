import socket
import Pyro4
import threading

def process_request(request_text):
    request_text = request_text.strip()

    if not request_text:
        return "ERROR: Empty request"

    parts = request_text.split()
    operation = parts[0].lower()

    math_service = Pyro4.Proxy("PYRONAME:mathserver")

    if operation == "add":
        if len(parts) != 3:
            return "ERROR: add requires 2 operands"
        a = float(parts[1])
        b = float(parts[2])
        result = math_service.add(a, b)

    elif operation == "sub":
        if len(parts) != 3:
            return "ERROR: sub requires 2 operands"
        a = float(parts[1])
        b = float(parts[2])
        result = math_service.sub(a, b)

    elif operation == "mul":
        if len(parts) != 3:
            return "ERROR: mul requires 2 operands"
        a = float(parts[1])
        b = float(parts[2])
        result = math_service.mul(a, b)

    elif operation == "div":
        if len(parts) != 3:
            return "ERROR: div requires 2 operands"
        a = float(parts[1])
        b = float(parts[2])
        result = math_service.div(a, b)

    elif operation == "mod":
        if len(parts) != 3:
            return "ERROR: mod requires 2 operands"
        a = float(parts[1])
        b = float(parts[2])
        result = math_service.mod(a, b)

    elif operation == "sqrt":
        if len(parts) != 2:
            return "ERROR: sqrt requires 1 operand"
        a = float(parts[1])
        result = math_service.sqrt(a)

    else:
        return f"ERROR: Unsupported operation '{operation}'"

    return f"RESULT: {result}"


def handle_client(client_socket, client_address):
    try:
        print(f"[Socket Server] Connected by {client_address}")

        data = client_socket.recv(1024)
        request_text = data.decode()
        print(f"[Socket Server] Received: {request_text}")

        response = process_request(request_text)
        client_socket.send(response.encode())
    except Exception as e:
        print(f"[Socket Server] Error handling client {client_address}: {e}")
    finally:
        client_socket.close()


def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP
    host = socket.gethostname()
    port = 9999
    serversocket.bind((host, port)) # Bind socket server to this host/port so clients can connect
    serversocket.listen()

    print(f"[Socket Server] Listening on {host}:{port}")
    print(f"[Socket Server] Waiting for client connections...")

    # Handle multiple clients using threads
    while True:
        client_socket, client_address = serversocket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()


if __name__ == "__main__":
    main()