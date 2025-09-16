import pika
import json

RABBIT_HOST = "rabbitmq"
EXCHANGE_NAME = "products_exchange"
QUEUE_NAME = "delete_product_reviews"
ROUTING_KEY = "product.deleted"

def send_delete_product_message(product_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))
    channel = connection.channel()

    # הגדרת exchange ו-queue
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct', durable=True)
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME, routing_key=ROUTING_KEY)

    message = {'product_id': product_id}
    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=ROUTING_KEY,
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2)  # persistent
    )
    connection.close()