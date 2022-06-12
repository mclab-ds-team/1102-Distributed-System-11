import json
import sys
import random

from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka import TopicPartition


ORDER_KAFKA_TOPIC = "orders"
ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(bootstrap_servers="localhost:29092")

consumer.assign([TopicPartition(ORDER_KAFKA_TOPIC, int(sys.argv[1]))])

producer = KafkaProducer(bootstrap_servers="localhost:29092")


print("Gonna start listening")
while True:
    for message in consumer:
        print("Ongoing transaction..")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)
        user_id = consumed_message["order_id"]
        total_cost = consumed_message["price"]

        data = {
            "order_id": user_id,
            "e-mail": consumed_message['e-mail'],
            "price": total_cost,
            "position": consumed_message['position'],
            "food": {
                "burger": consumed_message['food']['burger'],
                "sandwich": consumed_message['food']['sandwich'],
                "cola": consumed_message['food']['cola']
            }
        }
        print("Successful transaction..")
        producer.send(ORDER_CONFIRMED_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
