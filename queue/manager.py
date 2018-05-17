# -*- coding: utf-8 -*-
"""
@author: v.villar
"""


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
        pass

    def delete_queue(self, queue_id):
        pass

    def all_queues(self):
        pass

    def get_queue(self):
        pass
