# Learning Kafka using Python and Docker

- This is kind of a refresher as I hadn't built Kafka producer/consumer from ground up - just used them.

## Starting project
- Clone this repo
- Start Docker Desktop and run:
    ```
        docker compose up --build
    ```
- Wait for up to a minute. You should see:
    - Producer writing to terminal (or logs) "Delivered: ..."
    - Consumer later writing to terminal "Received: ..."
    - There might be delay between these


### The manual way to start Kafka using command prompt (Windows) - without Python

- Run docker: `docker compose up`
- Create topic: `docker exec -it <container-id> /opt/kafka/bin/kafka-topics.sh --create --topic test --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
- Create producer: `echo "Hello Kafka" | docker exec -i 978328d9996f /opt/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test`
- Create consumer: `docker exec -it <container-id> /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning`


## Basic things about Kafka

- Kafka runs as a cluster of servers (called brokers). We use Docker to simplify local setup.
    - Kafka requires Zookeeper (for coordination), though newer versions are moving toward KRaft (no Zookeeper).
- Kafka can have multiple topics, for example, 'clients', 'orders' etc.
- Topics are divided into partitions — this enables scalability and parallelism.
    - This example only uses one partition
- A producer can produce records on these topics
- The consumer can then consume whatever the produced produces
- Kafka is asynchronous and durable — messages are stored until consumed or expired.


# Why use Kafka

- Decoupling of systems
- Reliable message delivery:
    - If consumer goes down, it can restart from the same point it left off when it is back online.
    - Kafka handles retries and delivery gurantees
- Replayability of data:
    - You can go through messages from the beginning
- Scaling without tight coupling:
    - If more consumers are needed in the future
- Async:
    - The sending system doesn't need to wait for a response before moving on to the next task