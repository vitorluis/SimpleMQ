# -*- coding: utf-8 -*-
"""
@author: v.villar
"""
import uuid
from multiprocessing import Process, Lock

import gevent

from events.types import EventTypes
from message.message import Message
from queues.exceptions import MaximumConsumersReachedException
from queues.stack import Stack


class Queue(Process):
    """
    Class which represents an queue, where it will be put data
    """
    queue_id = None
    name = None
    stack = None
    lock = None
    consumers = None
    consumer_type = None
    max_consumers = None
    max_data_size = None
    event_dispatcher = None

    # Some constants for this class
    CONSUMER_NOTIFY_ALL = 0x1
    CONSUMER_INTERLEAVED = 0x2

    def __init__(self, name, max_consumers, max_data_size, consumer_type, event_dispatcher):
        """
        Class constructor
        :param event_dispatcher
        :type event_dispatcher: events.dispatcher.EventDispatcher
        """
        # Call the parent
        Process.__init__(self)

        # Create a new stack for queue and also create an ID
        self.queue_id = str(uuid.uuid4().hex)
        self.name = name
        self.max_consumers = max_consumers
        self.max_data_size = (max_data_size * 1024) * 1024
        self.event_dispatcher = event_dispatcher

        # Check the notification type
        if consumer_type == "notify_all":
            self.consumer_type = Queue.CONSUMER_NOTIFY_ALL
        elif consumer_type == "interleaved":
            self.consumer_type = Queue.CONSUMER_INTERLEAVED
        else:
            # By default, notify all consumers
            self.consumer_type = Queue.CONSUMER_NOTIFY_ALL

        # Stack requires a lock object
        self.lock = Lock()
        self.stack = Stack(self.lock, self.max_data_size)

        # Create a list of consumers
        self.consumers = []

        # Add an event listener here, when client disconnects, remove the consumer
        self.event_dispatcher.add_event_listener(EventTypes.ON_CLIENT_DISCONNECTED, self.client_disconnected)

    def register_consumer(self, consumer):
        """
        Register a new consumer for this Queue
        :param consumer:
        :type consumer: consumer.Consumer
        :return:
        """

        # We should check if we can add a new consumer to this queue
        if self.max_consumers == -1 or len(self.consumers) < self.max_consumers:
            self.consumers.append(consumer)
            return True

        # Otherwise, we should throw an exception
        raise MaximumConsumersReachedException()

    def remove_consumer(self, consumer):
        """
        Remove the Consumer from the queue
        :param consumer:
        :return:
        """
        self.consumers.remove(consumer)
        return True

    def publish_message(self, message):
        """
        Publish a new message in the Queue
        :param message:
        :return:
        """
        # Create the new message
        message = Message(message)

        # Put it on the Stack
        self.stack.write(message)

        # Notify the consumers about this change
        self._notify_consumers()

        # Return to the caller, if something happens, the caller will get an exception
        return True

    def _notify_consumers(self):
        """
        Notify the consumers about the new message
        :return:
        """
        # First we need to get the message to be delivered
        message = self.stack.read()

        # Lock it, to ensure that the consumers will receive the message in the right order
        self.lock.acquire()

        # We need to check which kind of notification it is
        if self.consumer_type == Queue.CONSUMER_NOTIFY_ALL:
            # Loop all consumers and send the message
            # Lets create gevent tasks to notify all consumers
            threads = []
            for consumer in self.consumers:
                threads.append(gevent.spawn(consumer.received_message, message))

            # Wait for everybody to be done
            gevent.joinall(threads)
        else:
            # Pick the caller which will get this notification
            if not self.consumers:
                self.lock.release()
                return

            # Get the next consumer which should receive the message
            consumer = self.consumers.pop(0)

            # Send the message
            consumer.received_message(message)

            # Put him back into the list
            self.consumers.append(consumer)

        # Free the lock
        self.lock.release()

    def client_disconnected(self, client):
        """
        Client disconnected, remove the consumer if has one
        :param client:
        :type client: server.client.Client
        :return:
        """
        # Get the consumer to be removed
        consumer = client.consumer

        # if has a consumer attached to it, remove it from our list
        if consumer is not None:
            # Acquire the lock, to be sure that while we are receiving messages
            # This consumer will not be eligible to send a message
            self.lock.acquire()

            # Remove it
            self.consumers.remove(consumer)

            # Release the lock and he process still go on :D
            self.lock.release()
