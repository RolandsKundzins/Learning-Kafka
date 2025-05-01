from confluent_kafka import Consumer, KafkaException
import os
import time

print("⏳ Consumer waiting for Kafka to be ready...")
time.sleep(15)
print("✅ Starting consumer...")

conf = {
    'bootstrap.servers': os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092'),
    'group.id': 'demo-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['orders'])

print("Consumer started. Listening to 'orders' topic...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        print(f"📦 Received: {msg.key().decode()} - {msg.value().decode()} from partition {msg.partition()}")

except KeyboardInterrupt:
    print("Stopping consumer...")

finally:
    consumer.close()
