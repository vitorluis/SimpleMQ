# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from commands.base import BaseCommand
from queues.consumer import Consumer


class ConsumerCommand(BaseCommand):
    """
    Producer class
    """
    signature = 'consumer'

    def run(self, client=None, *args):
        """
        Run the command
        :param args:
        :param client:
        :return:
        """
        # Create a consumer
        consumer = Consumer(client)
        return consumer
