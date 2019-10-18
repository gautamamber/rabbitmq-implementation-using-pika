import pika

# connect with rabbitMQ server

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# check queue exists

channel.queue_declare(queue='hello')

# Receiving messages from the queue is more complex. 
# It works by subscribing a callback function to a queue. 
# Whenever we receive a message, this callback function 
# is called by the Pika library. 

def callback(ch, method, properties, body):
    print(" [X] Recieved %r" % body)

channel.basic_consume(
    queue= "hello", on_message_callback= callback, auto_ack = True
    )
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

