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
    message_id = None
    data = None
    created_at = None

    def __init__(self, message, message_id=None, created_at=None):
        """
        Class constructor
        """
        # Set the message
        self.data = message

        # Create an ID and get the create date for this message
        if message_id is None:
            self.message_id = str(uuid.uuid4().hex)
        else:
            self.message_id = message_id

        if created_at is None:
            self.created_at = pendulum.now('UTC').timestamp()
        else:
            self.created_at = created_at

    def __str__(self):
        """
        Stringify the message
        :return:
        """
        data = {"id": self.message_id, "message": self.data, "created_at": self.created_at}
        return json.dumps(data)
