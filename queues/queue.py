# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import multiprocessing
import uuid
from multiprocessing import Process

from message.message import Message
from queues.stack import Stack


class Queue(Process):
    """
    Class which represents an queue, where it will be put data
    """
    id = None
    name = None
    stack = None
    lock = None
    consumers = None
    consumer_type = None
    max_consumers = None
    max_data_size = None

    # Some constants for this class
    CONSUMER_NOTIFY_ALL = 0x1
    CONSUMER_INTERLEAVED = 0x2

    def __init__(self, name, max_consumers, max_data_size, consumer_type):
        """
        Class constructor
        """
        # Call the parent
        Process.__init__(self)

        # Create a new stack for queue and also create an ID
        self.id = str(uuid.uuid4().hex)
        self.name = name
        self.max_consumers = max_consumers
        self.max_data_size = max_data_size
        self.consumer_type = consumer_type

        # Stack requires a lock object
        self.lock = multiprocessing.Lock()
        self.stack = Stack(self.lock)

        # Create a list of consumers
        self.consumers = []

    def register_consumer(self, consumer):
        """
        Register a new consumer for this Queue
        :param consumer:
        :type consumer: consumer.Consumer
        :return:
        """
        self.consumers.append(consumer)
        return True

    def remove_consumer(self, consumer):
        """
        Remove the Consumer from the queue
        :param consumer:
        :return:
        """
        self.consumers.remove(consumer)

    def publish_message(self, message):
        # Create the new message
        message = Message(message)

        # Put it on the Stack
        self.stack.write(message)

        # Notify the consumers
        self.notify_consumers(message)
        return True

    def notify_consumers(self, message):
        for consumer in self.consumers:
            consumer.received_message(message)
