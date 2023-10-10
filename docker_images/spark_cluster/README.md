# Building the Spark Cluster 
The Spark Cluster will be composed of these (stacked) images, starting from the `cluster_base` image as the base and going all the way up to `spark_worker`.

- spark_worker
- spark_master
- spark_base (<------- On top of `cluster_base`, we add the spark-hadoop package)
- cluster_base (<---- This is our first image, the base of our conatiner, it represents the OS & Python)


