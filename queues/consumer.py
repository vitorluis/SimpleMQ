# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import uuid


class Consumer:
    """
    Class responsible to manage a consumer client
    """
    id = None
    client = None

    def __init__(self, client):
        """
        Class constructor
        :param client:
        :type client: server.client.Client
        """
        self.id = str(uuid.uuid4().hex)
        self.client = client

    def received_message(self, message):
        """
        Received a message from the Queue
        :param message:
        :return:
        """
        self.client.send_response(str(message))
