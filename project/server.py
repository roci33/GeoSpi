import socket as s


class Server:
    def __init__(self):
        # Set var
        self.host = "localhost"
        self.port = 8080
        self.set_server()

    # Function to start server and start listen message from client
    def set_server(self):
        with s.socket() as server:
            server.bind((self.host, self.port))
            print("Server creato")
            server.listen()
            print("Server in ascolto")
            conn, add = server.accept()
            print(f"<-----------Vittima trovata, connessione stabilita! info: {add}----------->")
            while True:
                data = conn.recv(1024)
                data = data.decode()
                print(data)


if __name__ == "__main__":
    Server()
