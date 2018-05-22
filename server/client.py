# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from queues.consumer import Consumer


class Client:
    """
    :param socket:
    :type socket: gevent._socket3.socket
    """
    socket = None
    address = None
    file_descriptor = None
    queue_manager = None
    queue = None
    consumer = None
    event_dispatcher = None

    def __init__(self, socket, address, queue_manager, event_dispatcher):
        """
        Class Constructor
        :param socket:
        :param address:
        :param queue_manager:
        :type queue_manager: queue.manager.QueueManager
        """
        self.socket = socket
        self.address = address
        self.queue_manager = queue_manager
        self.event_dispatcher = event_dispatcher

    def listen(self):
        """
        Function to listen the commands client will enter
        :return:
        """
        # Subscribe for test purposes
        self.consumer = Consumer(self)
        self.queue = self.queue_manager.get_queue("myNewQueue")
        self.queue.register_consumer(self.consumer)
        # self.queue.publish_message("Something")

        self.file_descriptor = self.socket.makefile('rb')

        # Infinite loop, to always read what the client says
        while True:
            content = self.file_descriptor.readline()
            if not content:
                # Client disconnected, close file and socket
                self.finish_connection()
                break

            # Handle here the command
            self.queue.publish_message(str(content))
            self.handle_command(content)

    def handle_command(self, content):
        """
        Handle the command
        :param content:
        :return:
        """
        pass

    def send_response(self, data):
        """
        Just send data back
        :param data:
        :return:
        """
        self.socket.send(str(data).encode())

    def finish_connection(self):
        """
        Finish the client connection
        :return:
        """
        # Close the file descriptor and socket file
        self.file_descriptor.close()
        self.socket.close()

        # If have any consumer, we should disconnect here
