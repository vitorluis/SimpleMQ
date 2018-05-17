# -*- coding: utf-8 -*-
"""
@author: v.villar
"""


class Stack:
    """
    This class is responsible to manage the items in the stack
    """
    messages = None
    lock = None

    def __init__(self, lock):
        """
        Class Constructor.
        :param lock:
        :type lock: multiprocessing.Lock
        """
        # Define the initial statuses
        self.messages = []
        self.lock = lock

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

        # Add the message
        self.messages.append(message)

        # Release the lock
        self.lock.release()

    def read(self):
        # Get the lock, to prevent changes in the stack while reading
        self.lock.acquire()

        # Read get the content
        message = self.messages.pop(0)

        # Release our lock
        self.lock.release()
        return message
