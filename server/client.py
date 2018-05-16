# -*- coding: utf-8 -*-
"""
@author: v.villar
"""


class Client:
    """
    :param socket:
    :type socket: gevent._socket3.socket
    """
    socket = None
    address = None

    def __init__(self, socket, address):
        self.socket = socket
        self.address = address

    def listen(self):
        """
        Function to listen the commands client will enter
        :return:
        """
        file_descriptor = self.socket.makefile('rb')

        # Infinite loop, to always read what the client says
        while True:
            content = file_descriptor.readline()
            if not content:
                # Client disconnected, close file and socket
                file_descriptor.close()
                self.socket.close()
                break

            self.send_response("Received.")

    def send_response(self, data):
        """
        Just send data back
        :param data:
        :return:
        """
        self.socket.send(str(data).encode())
