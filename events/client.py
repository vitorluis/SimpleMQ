# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from events.events import Events


class ClientEvents(Events):
    """
    Class to define client connections
    """
    __events__ = ('on_client_disconnected',)
