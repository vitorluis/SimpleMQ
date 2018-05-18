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

    def __init__(self, name):
        """
        Class constructor
        """
        # Call the parent
        Process.__init__(self)

        # Create a new stack for queue and also create an ID
        self.id = str(uuid.uuid4().hex)
        self.name = name

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

    def publish_message(self, message):
        message = Message(message)
        self.stack.write(message)
        self.notify_consumers(message)
        return True

    def notify_consumers(self, message):
        for consumer in self.consumers:
            consumer.received_message(message)
