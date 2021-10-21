from kafka import KafkaConsumer


TOPIC_NAME = "Persons"
KAFKA_SERVER = "localhost:29092"

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)

for message in consumer:
    print(message)

