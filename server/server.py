# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from multiprocessing import Process

from gevent.server import StreamServer

from config.config import Config
from server.client import Client


class SimpleMQServer(Process):
    """
    Class responsible to run the server to accept connections
    """
    server = None
    config = None
    host = "0.0.0.0"
    port = 0
    queue_manager = None
    event_dispatcher = None

    def __init__(self, queue_manager, event_dispatcher):
        """
        Class constructor
        :param queue_manager:
        """
        # Call the parent
        Process.__init__(self)

        # Parse the config
        self.config = Config().get_config()
        self.port = self.config["server"]["port"]

        # Setup the queue manager
        self.queue_manager = queue_manager

        self.event_dispatcher = event_dispatcher

    def run(self):
        """
        Start the server
        :return:
        """
        self.create_socket()

    def create_socket(self):
        """
        Create the socket to receive the connection
        :return:
        """
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
        client = Client(socket, address, self.queue_manager, self.event_dispatcher)
        client.listen()
