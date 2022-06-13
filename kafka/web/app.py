import json
from sqlite3 import enable_callback_tracebacks
import time
from flask import Flask
from flask import render_template
from flask import request
import uuid
import random

from kafka import KafkaProducer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


ORDER_KAFKA_TOPIC = "orders"

producer = KafkaProducer(bootstrap_servers="localhost:29092", acks="all")

def send_kafka(id, pos, food1, food2, food3):
    data = {
        "order_id": str(uuid.uuid1()),
        "e-mail": f"{id}",
        "price": food1*6 + food2*5 + food3*2 ,
        "position": pos,
        "food":{
            "burger": food1,
            "sandwich": food2,
            "cola": food3
        }
    }

    producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    producer.flush()
    print(f"Done Sending..")
    # time.sleep(10)


@app.route('/', methods = ['POST', 'GET'])
def submit():
    global bottom_pross
    if request.method == 'POST':
        if request.values['Submit'] == '確認送出':
            user_id = request.values['user_id']
            position = request.values['p1']
            food_burger = int(request.values['burger'])
            food_sandwich = int(request.values['sandwich'])
            food_cola = int(request.values['cola'])
            send_kafka(user_id, position, food_burger, food_sandwich, food_cola)
    return render_template('home.html')



if __name__ == "__main__":
    app.run('0.0.0.0')