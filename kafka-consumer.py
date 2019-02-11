from kafka import KafkaConsumer

print('---running consumer')
consumer = KafkaConsumer('foo',bootstrap_servers='kafka:9092',auto_offset_reset='earliest')
print(consumer.fetch_messages)
for msg in consumer:
    print(msg)
print('kafke-exec-done')