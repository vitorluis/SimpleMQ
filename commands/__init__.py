# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import os

# Get a list of current py files of the current dir
modules = os.listdir(os.path.dirname(__file__))

# Get rid of the modules manager and __init__.py
modules.remove('manager.py')
modules.remove('__init__.py')

# Iterate into modules to remove the .py from the name
modules = [m.replace('.py', '') for m in modules]

# Add it, so in this way the commands will be plug and play style
__all__ = modules
