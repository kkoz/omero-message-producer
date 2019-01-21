# Omero Message Producer

## Simple Message Producer for Omero Message Consumer
This message producer allows the user to send messages to RabbitMQ which can then be consumed by an Omero Message Consumer.
To send messages:
 * Clone repository
 * cd into the top dir (`cd omero-message-producer`)
 * Update `message_producer.cfg` with the correct url, exchange, and queue name
 * Create Virtual Env (`virtualenv venv`)
 * Activate Virtual Env (`. venv/bin/activate`)
 * Install the message producer (`pip install .`)
 * run `send_message message_consumer.cfg path/to/files`
