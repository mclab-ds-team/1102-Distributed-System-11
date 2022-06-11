import json

from kafka import KafkaConsumer


ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"


consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092"
)

food_dict = {"burger": 0, "sandwich": 0, "cola": 0}
total_orders_count = 0
total_revenue = 0
print("Gonna start listening")
while True:
    # data = {
    #         "order_id": i,
    #         "user_id" : f"tom_{i}",
    #         "price"   : i * 5,
    #         "items"   : "burger,sandwich",
    #         "food"    :{ "burger": 3,
    #                      "cola": 1   }
    #         }
    for message in consumer:
        print("Updating analytics..")
        consumed_message = json.loads(message.value.decode())
        total_orders_count += 1
        total_revenue += float(consumed_message["price"])
        # print(consumed_message)
        food = consumed_message["food"]
        for i in food:
            food_dict[i] += consumed_message["food"][i]
        food_sort = sorted(food_dict.items(), key=lambda x:x[1], reverse=True)
        # print(food)
        print(f"bestseller 1st : {food_sort[0][0]}, 2nd : {food_sort[1][0]}, 3rd : {food_sort[2][0]}")
        print(f"Orders so far today: {total_orders_count}")
        print(f"Revenue so far today: {total_revenue}")

