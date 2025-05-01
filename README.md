# Learning Kafka

- Run docker: `docker compose up`
- Create topic: `docker exec -it <container-id> /opt/kafka/bin/kafka-topics.sh --create --topic test --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
- Create producer: `echo "Hello Kafka" | docker exec -i 978328d9996f /opt/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test`
- Create consumer: `docker exec -it <container-id> /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning`


## Some things

- Kafka runs as a cluster of servers (called brokers). We use Docker to simplify local setup.
    - Kafka requires Zookeeper (for coordination), though newer versions are moving toward KRaft (no Zookeeper).
- Kafka can have multiple topics, for example, 'clients', 'orders' etc.
- Topics are divided into partitions — this enables scalability and parallelism.
    - This example only uses one partition
- A producer can produce records on these topics
- The consumer can then consume whatever the produced produces
- Kafka is asynchronous and durable — messages are stored until consumed or expired.