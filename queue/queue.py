# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from multiprocessing import Process


class Queue(Process):
    """
    Class which represents an queue, where it will be put data
    """

    def __init__(self):
        Process.__init__(self)

    def register_consumer(self, consumer):
        pass

    def publish_message(self, message):
        pass
