# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from gevent import monkey

from events.dispatcher import EventDispatcher
from queues.manager import QueueManager
from server.server import SimpleMQServer

monkey.patch_all(subprocess=True)

if __name__ == "__main__":
    # Create the event dispatcher
    EVENT_DISPATCHER = EventDispatcher()
    EVENT_DISPATCHER.start()

    # Bind events
    EVENT_DISPATCHER.add_event("client_disconnected")

    # Create the queue manager
    QUEUE_MANAGER = QueueManager(EVENT_DISPATCHER)
    QUEUE_MANAGER.setup()

    # Start listen for connections
    SERVER = SimpleMQServer(QUEUE_MANAGER, EVENT_DISPATCHER)
    SERVER.start()
