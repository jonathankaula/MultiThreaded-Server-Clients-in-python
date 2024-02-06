import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode("utf-8")
        if not message:
            break

        print(f"Received from {client_address}: {message}")

        # Send acknowledgment back to client
        client_socket.send("Message received".encode("utf-8"))

    print(f"Client {client_address} disconnected")
    client_socket.close()

# Server configuration
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5555

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    # Accept client connection
    client_socket, client_address = server_socket.accept()

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
