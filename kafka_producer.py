
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    message = {"rule": "If transaction > 10000 then flag for review."}
    producer.send('fraud_rules', message)
    print(f"Produced: {message}")
    time.sleep(5)
