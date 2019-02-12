# kafka-python
simple kafka pub-sub using python

Aim of Sample:
- Dockerfile: creates a simple Linux machine with Python and kafka-python library installed
- kafka-producer.py: sent simple text message to Topic "foo"
- kafka-consumer.py: receives message from Topic "foo" and print it

How to run sample:
- Expecting you have Docker engine in your development machine
- Build a linux image with kafka-python library to run our consumer and producer code
- Run docker build command as follows
  - docker build .
- Run Zookeeper with command
  - docker run \
    --net=confluent \
    --rm confluentinc/cp-kafka:5.1.0 \
    kafka-topics --create --topic foo --partitions 1 --replication-factor 1 \
    --if-not-exists --zookeeper zookeeper:2181
Confirm zookeeper is working using command
  - docker logs zookeeper
  
- Run Kafka with command
  - docker run -d \
    --net=confluent \
    --name=kafka \
    -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092 \
    -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
    confluentinc/cp-kafka:5.1.0
 Confirm Kafka is running
  - docker logs kafka
 Run the Consumer application, this will run continuously until terminated using CTRL + C
  - docker run -v /Users:/Users --net=confluent -v /Users:/work work-stn-kafka:v0.2 python /Users/nazeels/python_scripts/kafka-producer.py
 Run following command to drop a few message to Kafka
  - docker run -v /Users:/Users --net=confluent -v /Users:/work work-stn-kafka:v0.2 python /Users/nazeels/python_scripts/kafka-consumer.py
 



Reference:
https://docs.confluent.io/current/installation/docker/docs/installation/single-node-client.html
https://kafka-python.readthedocs.io/en/master/index.html
