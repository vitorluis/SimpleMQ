# SimpleMQ
============

SimpleMQ is a message queue system maintained In-memory. 

## The idea

The main goal of SimpleMQ is to provide a message queue system easy to configure and fast to use.

Basically is a mix of Redis Pub/Sub where all subscribers receive the published message, and RabbitMQ where you can have multiple consumers and the broker interleaves the consumption between the subscribed consumers.

The second goal is to save the messages In-memory, so thd read/write is really fast, but insuring the atomicity of the queue.