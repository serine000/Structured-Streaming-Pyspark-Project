## Kafka Compose File Breakdown

The docker-compose file in this folder is meant to start up a kafka container and a zookeeper container.

Apache ZooKeeper is an open-source distributed coordination service.

Pairing Kafka and ZooKeeper containers is a best practice for deploying Kafka in a distributed and production-ready manner, as it provides the necessary infrastructure for Kafka's distributed coordination and management features.

Technically you could start a Kafka container on its own without ZooKeeper, doing so would result in a standalone Kafka instance with limited capabilities and no distributed coordination.

### Breaking down the kafka environment variables:
- KAFKA_BROKER_ID: Unique identifies each Kafka broker in a cluster [required].
- KAFKA_LISTENERS: Specifies the the network listeners on which Kafka will accept incoming connections [required].
It allows you to configure different listeners for various network interfaces and ports. The format for defining listeners is protocol://host:port.
It complements `KAFKA_ADVERTISED_LISTENERS`.
- KAFKA_ZOOKEEPER_CONNECT: Specifies the zookeeper connection string for Kafka to coordinate with ZooKeeper [required].
- KAFKA_ADVERTISED_LISTENERS: Defines how clients should connect to Kafka brokers [required].
- KAFKA_LISTENERS_SECURITY_PROTOCOL_MAP: Maps listeners to security protocols. For example, you can map to a plaintext listener to `PLAINTEXT` or to the SSL listener with `SSL` [required if you have listeners using different security protocols]. Note that using the PLAINTEXT security protocol implies that the Kafka connections are not encrypted or authenticated. 
- KAFKA_INTER_BROKER_LISTERNER_NAME: Specifies the listener name used for communication between Kafka brokers [required if you have multiple listeners, and you want to specify which one brokers should use for inter-broker communication.].
- KAFKA_LOG_RETENTION_HOURS: Configures the log retention policy in hours.[optional for fine-tuning].
- ALLOW_PLAINTEXT_LISTENER: Allows the creation of listeneres that use the `PLAINTEXT` security network protocol.
- KAFKA_AUTO_CREATE_TOPICS_ENABLE: Enables Kafka's topic auto-creation feature which allows Kafka to automatically create topics when a producer or consumer attempts to use a topic that doesn't already exist.

### Kafka topic creation
To create a kafka topic, follow these steps:
1. Ensure that your kafka container is up and running by simply running `docker-compose up -d`
2. Enter your container with `docker exec -it kafka bash`
3. Navigate to where the kafka scripts are located using `cd/kafka_2.13-2.8.1/bin` (the kafka version number in the dir name might differ, but that's fine).
4. Run `kafka-topics.sh --create --topic TOPIC_NAME --partitions 1 --replication-factor 1 --zookeeper zookeeper:2181` to create your own topic inside the kafka container by inserting your topic's name in the place of TOPIC_NAME in the instruction above.



