# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from multiprocessing import Process

from gevent.server import StreamServer

from config.config import Config
from server.client import Client


class SimpleMQServer(Process):
    server = None
    config = None
    host = "0.0.0.0"
    port = 0

    def __init__(self):
        # Call the parent
        Process.__init__(self)

        # Parse the config
        self.config = Config().get_config()
        self.port = self.config["server"]["port"]

    def run(self):
        self.create_socket()

    def create_socket(self):
        # Create the socket with the configuration
        self.server = StreamServer((self.host, self.port), self.client_connected)
        self.server.serve_forever()

    def client_connected(self, socket, address):
        """
        :param socket:
        :type socket:gevent._socket3.socket
        :param address:
        :type address: tuple
        :return:
        """
        # Client is now connected, and this is already a GreenLet
        socket.sendall('Welcome to SimpleMQ \n'.encode())

        # And now create a client and listen the data
        client = Client(socket, address)
        client.listen()
