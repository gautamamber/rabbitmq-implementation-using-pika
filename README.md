### RabbitMQ

# RabbitMQ is used to send and recieve messages. It works on the principle of message broker and its mechanics.

## Terminologies in RabbitMQ

1. Producers: It sends messages, hence creating message is producing.
2. Consumer: It recieve message, hence recieving messages is consuming.
3. Queue: It is a buffer in which sent messages are stored and ready to be recieve. There is no limitation to how many messages a single queue can hold. This is also no limitation
as to how many Producer can send a message to a queue. It  waits there until consumed by a Consumer.
4. Exchange: It is an entity that resides down between producers and queues. The producer never sends a message directly to a queue. It sends messages to an exchange, which - in turn - places the message to one or more queues, depending on the
 exchange used.
5. Binding is a connection between queues and exchanges. Queues bound to a certain exchange are served by the exchange. How exactly depends on the exchange itself.

## Protocols

RabbitMQ speaks multiple protocols. This tutorial uses AMQP 0-9-1, which is an open, general-purpose protocol for messaging.

[Visit this link for more](https://www.rabbitmq.com/)