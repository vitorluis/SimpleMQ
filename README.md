# SimpleMQ

SimpleMQ is a message queue system keeping the data In-memory. 

## The idea

The main goal of SimpleMQ is to provide a message queue system easy to configure and fast to use. You cam configure the queues easily by a JSON file witn the queue information.

SimpleMQ basically is a mix of Redis Pub/Sub where all subscribers receive the published message, and RabbitMQ where you can have multiple consumers and the broker interleaves the consumption between the subscribed consumers.

So you can configure each queue to behave differently, one could be configured to notify all consumers or interleave the consumption.

## Other goals

The second goal is to save the messages In-memory, so thd read/write is really fast, but insuring the atomicity of the queue.

## Tech behind it

We are developing the SimpleMQ in Python using Gevent for concurrent processing.

## Final notes

SimpleMQ its not being created to replace RabbitMQ or Kafka (At least, Not for a short term). But you can quickly setup and use in your application, without exchanges, topics (From RabbitMQ and Kafka) or partitions (from Kafka).

## Contributors
Vitor Villar - Main Developer <vitor.luis98@gmail.com>