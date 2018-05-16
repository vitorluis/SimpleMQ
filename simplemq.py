# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from gevent import monkey

from server.server import SimpleMQServer

monkey.patch_all(subprocess=True)

if __name__ == "__main__":
    server = SimpleMQServer()
    server.start()
