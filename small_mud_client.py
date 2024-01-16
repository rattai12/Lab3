import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # Connect to the server at localhost and port 12345

    finished = False
    print("Welcome to the simple MUD, the simple Multi-User Dungeon game.")
    while not finished:
        command = input(': ')
        if command.lower() in ["quit", "q"]:
            finished = True
            client_socket.sendall(command.encode())  # Send 'quit' command to server before closing
        else:
            client_socket.sendall(command.encode())  # Send command to server

            # Receive and print response from server
            response = client_socket.recv(1024).decode('utf-8')
            print(response)

    client_socket.close()

if __name__ == "__main__":
    start_client()
