import socket
import selectors


SELECTOR = selectors.DefaultSelector()
CONNECTIONS = {}

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 5000))
    server_socket.listen()

    SELECTOR.register(
        fileobj=server_socket,
        events=selectors.EVENT_READ,
        data=accept_connection
    )


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print("Connection from: ", addr)

    SELECTOR.register(
        fileobj=client_socket,
        events=selectors.EVENT_READ,
        data=send_message
    )
    CONNECTIONS[client_socket] = addr


def send_message(client_socket: socket.socket):
    request = client_socket.recv(4096)
    if request:
        response = b"Hello world\n"
        client_socket.send(response)
    else:
        SELECTOR.unregister(client_socket)
        client_socket.close()
        print(f"Connection with {CONNECTIONS[client_socket]} closed.")
        del CONNECTIONS[client_socket]


def event_loop():
    while True:
        events = SELECTOR.select()

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == "__main__":
    server()
    event_loop()
