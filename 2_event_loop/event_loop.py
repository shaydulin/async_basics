import socket
from select import select

TO_MONITOR = []
CONNECTIONS = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 5000))
server_socket.listen()
TO_MONITOR.append(server_socket)


def accept_connection(server_socket: socket.socket):
    client_socket, addr = server_socket.accept()
    print("Connection from: ", addr)
    TO_MONITOR.append(client_socket)
    CONNECTIONS[client_socket] = addr


def send_message(client_socket: socket.socket):
    request = client_socket.recv(4096)
    if request:
        response = b"Hello world\n"
        client_socket.send(response)
    else:
        client_socket.close()
        TO_MONITOR.remove(client_socket)
        print(f"Connection with {CONNECTIONS[client_socket]} closed.")
        del CONNECTIONS[client_socket]


def event_loop():
    while True:
        ready_to_read, _, _ = select(TO_MONITOR, [], [])

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == "__main__":
    event_loop()
