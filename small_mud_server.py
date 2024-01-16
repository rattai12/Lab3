import socket


Current_room = 0

description = [
    "You see a typical class room with a whiteboard in front of you.",
    "You are in a corridor at University West.",
    "You see a restaurant where people eat breakfast.",
    "Oh no, Thomas Office! Back away"]


def parse_and_execute(command):
    global Current_room
    if command == "look" or command == "l":
        return description[Current_room]
    if command == "go east" or command == "e":
        if Current_room < 2:
            Current_room += 1
            return "You walk east!"
        return "You bump into the wall!"
    if command == "go west" or command == "w":
        if Current_room > 0:
            Current_room -= 1
            return "You walk west!"
        return "You bump into the wall!"
    if command == "go north" or command == "n":
        if Current_room < 3:
            Current_room -= 1
            return "You walk north!"
        return "You bump into the wall!"
    

    if command == "help" or command == "h" or command == "?":
        return "Try looking around, go east, west, north or quit!"
    return "I don't understand your command!"



def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))  # Host and port
    server_socket.listen()

    print("Server is listening for connections...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established.")

    client_socket.send(bytes("Welcome to the simple MUD server!", "utf-8"))

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            print(f"Received from client: {message}")
            response = parse_and_execute(message)
            client_socket.send(bytes(response, "utf-8"))
        else:
            break

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()





