from confluent_kafka import Consumer
print("Consumer started...")
c = Consumer({
    'bootstrap.servers': 'kafka:9092',  # Updated to match service name
    'group.id': 'vitals-group',
    'auto.offset.reset': 'earliest'
})
c.subscribe(['vital_signs'])

print("Consumer started...")
while True:
    msg = c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue
    print(f"Consumed: {msg.value().decode('utf-8')}")
c.close()
