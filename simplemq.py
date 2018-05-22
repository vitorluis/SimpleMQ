# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from gevent import monkey

from queues.manager import QueueManager
from server.server import SimpleMQServer

monkey.patch_all(subprocess=True)

if __name__ == "__main__":
    # Create the queue manager
    QUEUE_MANAGER = QueueManager()
    QUEUE_MANAGER.setup()

    # Start listen for connections
    SERVER = SimpleMQServer(QUEUE_MANAGER)
    SERVER.start()
