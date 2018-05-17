# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from queue.queue import Queue


class QueueManager:
    """
    QueueManager is responsible to manage all queues configured in the system
    """
    queues = None

    def __init__(self):
        """
        Class constructor
        """
        # Setup the initial attrs
        self.queues = []

    def add_queue(self, config):
        # For tests purposes, create a queue here
        q = Queue("newQueue")
        self.queues.append(q)

    def delete_queue(self, queue_id):
        pass

    def all_queues(self):
        return self.queues

    def get_queue(self):
        return self.queues[0]
