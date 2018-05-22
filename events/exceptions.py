# -*- coding: utf-8 -*-
"""
@author: v.villar
"""


class EventNotFoundException(Exception):
    """
    Event not found in the dispatcher
    """
    pass


class EventAlreadyExistsException(Exception):
    """
    Event already exists
    """
    pass
