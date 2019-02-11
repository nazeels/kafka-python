from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka:9092')
for _ in range(100):
    producer.send('foo', b'---nazeel')
print('kafka producer')