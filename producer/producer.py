from confluent_kafka import Producer
import os
import random
import time

print("⏳ Producer waiting for Kafka to be ready...")
time.sleep(15)
print("✅ Starting producer...")

def error_cb(err):
    print(f"❌ Kafka error: {err}")


bootstrap_servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
print(f"Using bootstrap servers: {bootstrap_servers}")

producer = Producer({
    'bootstrap.servers': bootstrap_servers,
    'error_cb': error_cb
})

print("✅ Producer created")

regions = ['US', 'EU', 'ASIA']

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered: {msg.key().decode()} - {msg.value().decode()} to {msg.topic()} [{msg.partition()}]")

for _ in range(10):
    print("Producing message...")
    region = random.choice(regions)
    value = f"Order from {region}"
    producer.produce('orders', key=region, value=value, callback=delivery_report)
    time.sleep(1)  # Simulate delay

producer.flush()
