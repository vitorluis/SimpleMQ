# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import json
import os

from queues.exceptions import QueueNotFoundException
from queues.queue import Queue


class QueueManager:
    """
    QueueManager is responsible to manage all queues configured in the system
    """
    queues = None
    queues_config = None
    config_path = None

    def __init__(self):
        """
        Class constructor
        """
        # Setup the initial attrs
        self.queues = []
        self.config_path = os.path.join(os.path.dirname(".."), "queues.json")

    def parse_queue_config(self):
        """
        Parse the queue config and create the queues
        """
        with open(self.config_path) as f:
            self.queues_config = json.load(f)

        """ Add each queue """
        for config in self.queues_config['queues']:
            self.add_queue(config)

    def add_queue(self, config):
        """
        Add a queue into the system
        :param config: Queue configuration
        :return:
        """
        # Create a new Queue to be transfer data
        q = Queue(config['name'], config['max_consumers'], config['max_data_size'], config['consumption_type'])

        # Add the queue to our queue list
        self.queues.append(q)
        return True

    def delete_queue(self, queue_id):
        """
        Delete a queue from the system
        :param queue_id:
        :return:
        """
        for queue in self.queues:
            if queue.id == queue_id:
                self.queues.remove(queue)
                return True

        # If didn't find any queue with this ID, throw an exception
        raise QueueNotFoundException("Queue with ID {} not found".format(queue_id))

    def all_queues(self):
        """
        return all queues
        :return: self.queues
        """
        return self.queues

    def get_queue(self, name):
        """
        Get a queue by its name
        :param name:
        :return:
        """
        return self._find_queue_by_name(name)

    def _find_queue_by_name(self, name):
        """
        Look into Queue list and find a queue with the given name
        :param name:
        :return:
        """
        for queue in self.queues:
            if queue.name == name:
                return queue

        # If didn't find any queue with this ID, throw an exception
        raise QueueNotFoundException("Queue with name {} not found".format(name))

    def setup(self):
        """
        Setup the Queue manager
        :return:
        """
        self.parse_queue_config()
