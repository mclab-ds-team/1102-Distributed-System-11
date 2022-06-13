import json
import time
import random
import sys

from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "orders"
ORDER_LIMIT = 10

producer = KafkaProducer(bootstrap_servers="localhost:29092")

# print("Going to be generating order after 10 seconds")
# print("Will generate one unique order every 10 seconds")
# time.sleep(10)

for i in range(1, ORDER_LIMIT):
    data = {
        "order_id": i,
        "e-mail": f"tom_{i}",
        "price": i * 5,
        "position": "政大",
        "food":{
            "burger": 3,
            "sandwich": 5,
            "cola": 1
        }
    }
    a = random.randint(0,int(sys.argv[1]))
    print(a)
    producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"), partition=a)
    print(f"Done Sending..{i}")
    time.sleep(10)
