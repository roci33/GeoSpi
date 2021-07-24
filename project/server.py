import socket as s


class Server:
    def __init__(self):
        self.host = "localhost"
        self.port = 8080
        self.set_server()

    def set_server(self):
        with s.socket() as server:
            server.bind((self.host, self.port))
            print("server creato")
            server.listen()
            print("server in ascolto")
            conn, add = server.accept()
            print(f"vittima trovata, connessione stabilita! info: {add}")
            while True:
                data = conn.recv(1024)
                data = data.decode()
                print(data)


if __name__ == "__main__":
    Server()
