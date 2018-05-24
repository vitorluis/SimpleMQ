# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from abc import abstractmethod


class BaseCommand:
    event_dispatcher = None
    signature = None

    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher

    @abstractmethod
    def run(self, client=None, *args):
        pass
