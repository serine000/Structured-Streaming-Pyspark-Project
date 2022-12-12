# Building the Spark Cluster 
As we know, we can stack several docker images one over the other (we basically build a stack of images).
So the way our Spark Cluster is set up is using these four images:
(Read this list from bottom to top)


- spark_worker
- spark_master
- spark_base (<------- On top of the OS now and since python is available, we add the spark-hadoop package)
- cluster_base (<---- This is our first image, the base of our conatiner: The OS & Python)


