



Created a file named `client.py` with the following content:

```python
import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 12345))

    # Receive a message from the server
    message = client_socket.recv(1024)
    print("Message from server:", message.decode())

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
```

### Step 3: Run the Application

1. **Start the server:**

   Open a terminal and run:

   ```bash
   python server.py
   ```

2. **Start the client:**

   Open another terminal and run:

   ```bash
   python client.py
   ```

### Output

When you run the client after starting the server, you should see:

```
Message from server: Hello from the server!
```

### Explanation

- **Server:**
  - Creates a socket and binds it to `localhost` on port `12345`.
  - Listens for incoming connections.
  - Sends a welcome message to the connected client.

- **Client:**
  - Creates a socket and connects to the server.
  - Receives the message from the server and prints it.

This simple example illustrates the basics of socket programming in Python. Feel free to expand on it for more complex interactions!
