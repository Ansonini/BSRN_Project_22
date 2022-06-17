import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4444
ADDRESS = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():
    print("[STARTING] Server is Starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen()
    print("[LISTENING] Server is Listening.")

    while True:
        connection, address = server.accept()
        print(f"[NEW CONNECTION] {address} connected.")

        filename = connection.recv(SIZE).decode(FORMAT)
        print("[RECV] File name received.")
        file = open(filename, "w")
        connection.send("Filename received.".encode(FORMAT))

        data = connection.recv(SIZE).decode(FORMAT)
        print(f"[RECV] File data received.")
        file.write(data)
        connection.send("File data received".encode(FORMAT))

        file.close()
        connection.close()
        print(f"[DISCONNECTED] {address} disconnected.")


if __name__ == "__main__":
    main()
