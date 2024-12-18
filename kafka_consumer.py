
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('fraud_rules', bootstrap_servers='localhost:9092', auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    print(f"Consumed: {message.value}")
