# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import json
import uuid

import pendulum


class Message:
    """
    Class which defines a message into the system
    """
    id = None
    data = None
    created_at = None

    def __init__(self, message):
        """
        Class constructor
        """
        # Set the message
        self.data = message

        # Create an ID and get the create date for this message
        self.id = str(uuid.uuid4().hex)
        self.created_at = pendulum.now('UTC').timestamp()

    def __str__(self):
        """
        Stringify the message
        :return:
        """
        return json.dumps({"id": self.id, "message": self.data, "created_at": self.created_at})
