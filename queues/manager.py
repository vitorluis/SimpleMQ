# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import json

from queues.queue import Queue


class QueueManager:
    """
    QueueManager is responsible to manage all queues configured in the system
    """
    queues = None
    queues_config = None

    def __init__(self):
        """
        Class constructor
        """
        # Setup the initial attrs
        self.queues = []

    def parse_queue_config(self):
        """
        Parse the queue config and create the queues
        """
        with open("../queues.json") as f:
            self.queues_config = json.load(f)

        """ Add each queue """
        for config in self.queues_config:
            self.add_queue(config)

    def add_queue(self, config):
        """
        Add a queue into the system
        :param config: Queue configuration
        :return:
        """
        # For tests purposes, create a queue here
        q = Queue("newQueue")
        self.queues.append(q)

    def delete_queue(self, queue_id):
        pass

    def all_queues(self):
        return self.queues

    def get_queue(self):
        return self.queues[0]
