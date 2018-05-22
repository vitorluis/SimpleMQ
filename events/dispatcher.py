# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import time
from multiprocessing import Process

import gevent

from events.exceptions import EventAlreadyExistsException, EventNotFoundException


class EventDispatcher(Process):
    """
    Class to dispatch event to the listeners
    """
    events = None

    def __init__(self):
        """
        Class constructor
        """
        Process.__init__(self)

        # Create a dictionary with the events
        self.events = {}

    def add_event(self, event):
        """
        Add new event to dispatch and be listened
        :param event:
        :return:
        """
        if event in self.events.keys():
            raise EventAlreadyExistsException("Already exists")

        # Add the event
        self.events.update({event: []})
        return True

    def add_event_listener(self, event, callback):
        """
        Add a new listener to some event
        :param event:
        :param callback:
        :return:
        """
        if event not in self.events.keys():
            raise EventNotFoundException("The event {} was not found".format(event))

        # Add the callback to the list to be called
        self.events[event].append(callback)
        return True

    def dispatch(self, event, data):
        """
        Dispatch an event with some data on it
        :param event:
        :param data:
        :return:
        """
        # Get the event
        if event not in self.events.keys():
            raise EventNotFoundException("The event {} was not found".format(event))

        # Get the listeners of this thing
        listeners = self.events[event]

        # Spawn a gevent process to call the listeners
        tasks = []
        for listener in listeners:
            tasks.append(gevent.spawn(listener, data))

            # Join all tasks and wait to finish it
            # gevent.joinall(tasks)

    def run(self):
        """
        Run the dispatcher
        :return:
        """
        while True:
            time.sleep(1)
