# Mongo Pyspark Clusters
## Quick description: 
  This project links together a MongoDB cluster with a Pyspark cluster. The next stage is to then stream data from Mongo to our Pyspark application for processing using spark structured streaming and write back the results to Mongo.
 
 ### Goals Summary:
 - Build Mongo cluster
 - Bild Pyspark Cluster
 - Stream from and back to Mongo using structured streaming.
  
## Structure:
(Note: This is a quick rundown of the structure, for a more detailed description of how this entire setup works, check out my Medium article, available for everyone: )
  - For MongoDB we have 3 containers (so 3 nodes where one will be our primary and the two others secondary).
  - For Pyspark we have our master node and two worker nodes.
  - All (6) containers belong to the same user-defined docker network so that they can communicate with each other.
  - For Structure steaming to be implemented in this configuration we will require the mongo-spark-connector version 10.0.5, which was released early 2022 to support structured streaming.
  - It is very important to have a ReplicaSet configuration in our Mongo Cluster for structured streaming to be implemented.
  
  
