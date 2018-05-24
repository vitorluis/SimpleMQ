# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import json
import os


class Config:
    """
    Class to handle the server config
    """
    config_dict = None

    def __init__(self):
        """
        Class constructor
        """
        # Parse the YAML
        config_file = os.path.join(os.path.dirname(".."), 'config.json')
        if not os.path.exists(config_file):
            config_file = os.path.join(os.path.dirname(__file__), '../config.json')

        with open(config_file) as file_opened:
            data = json.load(file_opened)

            # Convert the dictionary into object
            self.config_dict = data

    def get_config(self):
        """
        return the config as dict
        :return:
        """
        return self.config_dict
