# -*- coding: utf-8 -*-
"""
@author: v.villar
"""


class QueueNotFoundException(Exception):
    """
    Queue not found
    """
    pass


class StackOverflowException(Exception):
    """
    Stack cannot accept more data
    """
    pass


class MaximumConsumersReachedException(Exception):
    """
    No more consumers allowed for this queue
    """
    pass
