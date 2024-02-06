import socket

# Client configuration
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5555

# Connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

while True:
    # Send message to server
    message = input("Enter message: ")
    client_socket.send(message.encode("utf-8"))

    # Receive acknowledgment from server
    response = client_socket.recv(1024).decode("utf-8")
    print(f"Server response: {response}")
