import pika
import json
import time
import logging

RABBIT_HOST = "rabbitmq"
EXCHANGE_NAME = "products_exchange"
QUEUE_NAME = "delete_product_reviews"
ROUTING_KEY = "product.deleted"

logger = logging.getLogger(__name__)

def send_delete_product_message(product_id):
    """
    Send a message to RabbitMQ with retry logic.

    Args:
        product_id (int): ID of the deleted product.
        retries (int): Number of retry attempts.
        delay (int): Delay between retries in seconds.
    """
    retries = 5
    delay = 2
    
    for attempt in range(1, retries + 1):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))
            channel = connection.channel()

            # Declare exchange and queue
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
            logger.info(f"Message sent for product_id {product_id}")
            return  
        except pika.exceptions.AMQPConnectionError as e:
            logger.warning(f"Attempt {attempt} failed to connect to RabbitMQ: {e}")
            time.sleep(delay)
    logger.error(f"Failed to send message for product_id {product_id} after {retries} attempts")