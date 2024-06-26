import pika

from constants import RMQ_ADDRESS, RMQ_PORT
from models.events import Event

def send_to_rmq(event: Event, data: str):
    try:
        # Establish a new connection
        connection = pika.BlockingConnection(pika.ConnectionParameters(RMQ_ADDRESS, port=RMQ_PORT))
        # Create a new channel
        channel = connection.channel()

        # Declare a topic exchange named 'main'
        channel.exchange_declare(exchange='main', exchange_type='topic')

        # Publish the message to the 'main' exchange with the specified routing key
        channel.basic_publish(exchange='main', routing_key=event.name, body=data)
        print(f"Sent {event.name} message: {data}")

    except Exception as e:
        print("Error:", e)
    finally:
        # Close the connection
        if connection:
            connection.close()
