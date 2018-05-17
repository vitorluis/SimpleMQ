# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from queue.consumer import Consumer
from queue.queue import Queue


class Client:
    """
    :param socket:
    :type socket: gevent._socket3.socket
    """
    socket = None
    address = None
    queue_manager = None
    queue = None

    def __init__(self, socket, address, queue_manager):
        """

        :param socket:
        :param address:
        :param queue_manager:
        :type queue_manager: queue.manager.QueueManager
        """
        self.socket = socket
        self.address = address
        self.queue_manager = queue_manager

        # For test purpose , get a queue here and publish something
        self.queue_manager.add_queue(Queue("myQueue"))
        self.queue = self.queue_manager.get_queue()

        # Also subscribe for consumption
        self.queue.register_consumer(Consumer(self))

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
            self.queue.publish_message("My content")
            print(content)

            # For test purposes, get the queue

    def send_response(self, data):
        """
        Just send data back
        :param data:
        :return:
        """
        self.socket.send(str(data).encode())
