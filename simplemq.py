# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
from gevent import monkey

from events.dispatcher import EventDispatcher
from events.types import EventTypes
from queues.manager import QueueManager
from server.server import SimpleMQServer

monkey.patch_all(subprocess=True)

if __name__ == "__main__":
    # Create the event dispatcher
    event_dispatcher = EventDispatcher()

    # Bind events
    event_dispatcher.add_event(EventTypes.ON_CLIENT_DISCONNECTED)

    # Create the queue manager
    queue_manager = QueueManager(event_dispatcher)
    queue_manager.setup()

    # Start listen for connections
    server = SimpleMQServer(queue_manager, event_dispatcher)
    server.start()
