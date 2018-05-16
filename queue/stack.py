# -*- coding: utf-8 -*-
"""
@author: v.villar
"""


class Stack:
    """
    This class is responsible to manage the items in the stack
    """
    writable = None
    readable = None
    items = None
    lock = None

    def __init__(self, lock):
        """
        Class Constructor.
        :param lock:
        :type lock: multiprocessing.Lock
        """
        # Define the initial statuses
        self.writable = True
        self.readable = True
        self.items = []
        self.lock = lock

    def write(self, item):
        # Check first if it is writable
        if self.is_writable():
            # Acquire the lock for this stack, to be sure that any other producer will write
            # In the same time
            self.lock.acquire()

    def read(self):
        pass

    def is_writable(self):
        return self.writable

    def is_readable(self):
        return self.readable
