import socket
from select import select


TASKS = []

TO_READ = {}
TO_WRITE = {}

CONNECTIONS = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 5000))
    server_socket.listen()

    while True:
        yield ("read", server_socket)
        client_socket, addr = server_socket.accept()
        print("Connection from: ", addr)
        CONNECTIONS[client_socket] = addr
        TASKS.append(client(client_socket))


def client(client_socket: socket.socket):
    while True:

        yield ("read", client_socket)
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = "Hello world\n"
            for r in response:
                yield ("write", client_socket)
                client_socket.send(r.encode())
    
    client_socket.close()
    print(f"Connection with {CONNECTIONS.pop(client_socket)} closed.")


def event_loop():
    while any([TASKS, TO_READ, TO_WRITE]):
        while not TASKS:
            ready_to_read, ready_to_write, _ = select(
                TO_READ,
                TO_WRITE,
                [],
            )

            for sock in ready_to_read:
                TASKS.append(TO_READ.pop(sock))
            for sock in ready_to_write:
                TASKS.append(TO_WRITE.pop(sock))
        
        try:
            task = TASKS.pop(0)
            to_do, sock = next(task)
            if to_do == "read":
                TO_READ[sock] = task
            if to_do == "write":
                TO_WRITE[sock] = task
        except StopIteration:
            pass


if __name__ == "__main__":
    TASKS.append(server())
    event_loop()
