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
    queue_manager = QueueManager()
    queue_manager.setup()

    # Start listen for connections
    server = SimpleMQServer(queue_manager)
    server.start()
