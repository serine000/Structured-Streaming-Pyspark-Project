## Kafka Compose File Breakdown

The docker-compose file in this folder is meant to start up a kafka container and a zookeepr container.

The function of zookeeper is to 


### Breaking down the kafka environment variables:
- KAFKA_ADVERTISED_LISTENERS: Defines how clients should connect to Kafka brokers.
- KAFKA_LISTENERS: Specifies the listeners for the broker. It complements KAFKA_ADVERTISED_LISTENERS.
- KAFKA_ZOOKEEPER_CONNECT: Specifies the ZooKeeper connection string for Kafka to coordinate with ZooKeeper.
- KAFKA_CREATE_TOPICS: Allows you to define topics and their configurations during container startup. This is particularly useful for automated topic creation.
- KAFKA_SSL_*: A group of environment variables for configuring SSL security if your Kafka cluster uses SSL.
- KAFKA_SASL_*: A group of environment variables for configuring SASL security if your Kafka cluster uses SASL.
- KAFKA_HEAP_OPTS: Allows you to specify Java heap options for Kafka brokers.
- KAFKA_LOG_DIRS: Sets the directory for Kafka log storage.
- KAFKA_LOG_RETENTION_HOURS: Configures the log retention policy in hours.