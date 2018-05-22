# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import os

import yaml


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
        config_file = os.path.join(os.path.dirname(".."), 'config.yaml')
        if not os.path.exists(config_file):
            config_file = os.path.join(os.path.dirname(__file__), '../config.yaml')

        with open(config_file) as file_opened:
            data = yaml.load(file_opened)

            # Convert the dictionary into object
            self.config_dict = data

    def get_config(self):
        """
        return the config as dict
        :return:
        """
        return self.config_dict
