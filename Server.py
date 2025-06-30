import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a host and port
    server_socket.bind(('localhost', 12345))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    # Accept a connection
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established!")

    # Send a welcome message to the client
    client_socket.send(b"Hello from the server!")

    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
  
