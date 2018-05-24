# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import inspect
import sys

from . import *


class CommandManager:
    """
    Class to handle commands
    """
    commands = {}
    event_dispatcher = None
    client = None

    def __init__(self, event_dispatcher, client):
        """
        Class Constructor
        :param event_dispatcher:
        """
        # Setup the event dispatcher
        self.event_dispatcher = event_dispatcher
        self.client = client

    def import_commands(self):
        """
        Method to import dynamically our commands
        :return:
        """
        commands = self._get_modules_list()

        # Import the needed classes
        for m in commands:
            for name, obj in inspect.getmembers(sys.modules['commands.{}'.format(m)]):
                if inspect.isclass(obj):
                    if obj.signature is not None:
                        self.commands.update({obj.signature: obj(self.event_dispatcher)})

    def handle(self, command):
        """
        Handle the command
        :param command:
        :return:
        """
        pass

    def _get_modules_list(self):
        """
        Get the list of modules
        :return:
        """

        # Get a list of current py files of the current dir
        modules = os.listdir(os.path.dirname(__file__))

        # Get rid of the modules manager and __init__.py
        modules.remove('manager.py')
        modules.remove('__init__.py')

        # Iterate into modules to remove the .py from the name
        modules = [m.replace('.py', '') for m in modules]
        return modules
