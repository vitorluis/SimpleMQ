# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import json
import sys

from message.message import Message
from queues.exceptions import StackOverflowException


class Stack:
    """
    This class is responsible to manage the items in the stack
    """
    messages = None
    lock = None
    max_data_size = None

    def __init__(self, lock, max_data_size):
        """
        Class Constructor.
        :param lock:
        :type lock: multiprocessing.Lock
        """
        # Define the initial statuses
        self.messages = []
        self.lock = lock
        self.max_data_size = max_data_size

    def write(self, message):
        """
        Write a message in the stack
        :param message: message to be stacked
        :param message: message.Message
        :return:
        """
        # Acquire the lock for this stack, to be sure that any other producer will write
        # In the same time
        self.lock.acquire()

        # Before append, check if the queue has enough space to save this item
        if sys.getsizeof(self.messages) >= self.max_data_size:
            self.lock.release()
            raise StackOverflowException("We don't have enough space to save this item")

        if (sys.getsizeof(message) + sys.getsizeof(self.messages)) > self.max_data_size:
            self.lock.release()
            raise StackOverflowException("We don't have enough space to save this item")

        # Add the message
        self.messages.append(str(message))

        # Release the lock
        self.lock.release()

    def read(self):
        """
        Read a message from the Stack
        :return:
        """
        # Get the lock, to prevent changes in the stack while reading
        self.lock.acquire()

        # Read get the content
        message = json.loads(self.messages.pop(0))
        message = Message(message['message'], message['id'], message['created_at'])

        # Release our lock
        self.lock.release()
        return message
