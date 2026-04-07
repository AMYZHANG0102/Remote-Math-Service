Distributed Math Service (Sockets + Pyro4 + Docker)
Overview

This project implements a distributed math service using a combination of:

TCP socket programming
Remote method invocation with Pyro4
Containerization using Docker

The system is designed to demonstrate how multiple services communicate across a network, separating responsibilities into independent components.

Users can send mathematical operations (e.g., add 5 3) from a client, which are processed remotely through a socket server and a Pyro-based backend service.

System Architecture

The system follows a layered, distributed architecture:

Client → Socket Server → Pyro Server
↓
Pyro Name Server

Components
1. Client (myclient.py)
Accepts user input from the terminal
Sends requests to the socket server using TCP
Receives and displays responses
Supports multiple requests in a single session
2. Socket Server (mysocketserver.py)
Listens for incoming TCP connections
Handles multiple clients concurrently using threads
Parses incoming requests (e.g., add 5 3)
Forwards requests to the Pyro server
Sends results back to the client
3. Pyro Server (pyroserver.py)
Implements mathematical operations:
add
sub
mul
div
mod
sqrt
Exposes methods using Pyro4
Registers itself with the Pyro Name Server
4. Pyro Name Server

Runs using:

python -m Pyro4.naming
Acts as a registry for remote objects
Maps a logical name (e.g., "mathserver") to the actual object location
Allows services to locate each other dynamically
Communication Flow
The client sends a request (e.g., add 5 3) to the socket server
The socket server parses the request
The socket server calls the Pyro server using a proxy
The Pyro server performs the operation
The result is returned to the socket server
The socket server sends the result back to the client
The client displays the result
Technologies Used
Python 3
TCP Socket Programming
Pyro4 (Remote Object Communication)
Multithreading (threading module)
Docker
Docker Compose
Key Concepts
Socket Programming

Used for communication between the client and the socket server. The client sends raw text requests over TCP, and the server processes them.

Pyro4 (Remote Method Invocation)

Allows the socket server to call methods on a remote object as if they were local:

math_service.add(a, b)

This abstracts away low-level networking.

Pyro Naming Service

Acts as a lookup system (similar to DNS):

Registers services:

ns.register("mathserver", uri)

Resolves services:

Pyro4.Proxy("PYRONAME:mathserver")
Multithreading

The socket server creates a new thread for each client connection, allowing multiple clients to be handled simultaneously.

Project Structure
project/
├── myclient.py
├── mysocketserver.py
├── pyroserver.py
├── requirements.txt
├── Dockerfile.client
├── Dockerfile.socketserver
├── Dockerfile.pyroserver
├── Dockerfile.pyronameserver
└── docker-compose.yml
Docker Architecture

Each component runs in its own container:

Container	Purpose
pyronameserver	Runs Pyro naming service
pyroserver	Hosts math operations
socketserver	Handles TCP client requests
client	Sends user input
How to Run
1. Build and start services
docker compose up --build
2. Run the client separately (recommended for interaction)
docker compose run --rm client
Example Usage
Enter your math operation (e.g., 'add 5 3'):
add 5 3

Output:

Server response: RESULT: 8.0
Supported Operations
add a b
sub a b
mul a b
div a b
mod a b
sqrt a
Error Handling

The system handles:

Invalid number of operands
Unsupported operations
Division by zero
Modulus by zero
Square root of negative numbers

Errors are returned as:

ERROR: <message>
Notes
Input must follow the correct format: operation + operands
The client supports multiple requests per session
The server uses threads to handle concurrent clients
Docker depends_on controls startup order but does not guarantee readiness
Summary

This project demonstrates how to:

Build a distributed system using multiple services
Combine socket programming with remote method invocation
Use Pyro4 for clean service communication
Containerize applications using Docker
Enable communication between services in a networked environment
