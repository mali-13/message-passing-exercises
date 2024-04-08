from kafka import KafkaProducer


TOPIC_NAME = 'orders'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'{"id": "ORD16", "created_by": "USR14", "status": "QUEUED", "created_at": "03-04-2024", "equipment": ["KEYBOARD", "MONITOR"]}')
producer.flush()
