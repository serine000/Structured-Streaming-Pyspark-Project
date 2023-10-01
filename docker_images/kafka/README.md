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
- KAFKA_LISTENERS_SECURITY_PROTOCOL_MAP: Maps listeners to security protocols. For example, you can map the plaintext listener to PLAINTEXT and the SSL listener to SSL [required if you have listeners using different security protocols].
KAFKA_INTER_BROKER_LISTERNER_NAME: Specifies the listener name used for communication between Kafka brokers [required if you have multiple listeners, and you want to specify which one brokers should use for inter-broker communication.].
- KAFKA_LOG_RETENTION_HOURS: Configures the log retention policy in hours.[optional for fine-tuning].
- KAFKA_CREATE_TOPICS: Allows you to define topics and their configurations during container startup. This is particularly useful for automated topic creation.
- KAFKA_LOG_RETENTION_HOURS: Configures the log retention policy in hours.
