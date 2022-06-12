from kafka.admin import KafkaAdminClient, NewTopic
from requests import delete


# admin_client = KafkaAdminClient({
#     "bootstrap.servers": "localhost:9092"
# })

# topic_list = []
# topic_list.append(NewTopic("order_details", 2, 1))
# admin_client.create_topics(topic_list)
# admin_client.delete_topics(['order_details',])



admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:29092"
)



topic_list = []
topic_list.append(NewTopic(name="orders", num_partitions=2, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)
print("created")