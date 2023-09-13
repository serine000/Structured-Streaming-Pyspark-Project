FROM cluster_base
# -- Now above the cluster_base (OS & python) image we add another image/building block for our Spark cluster
# -- We add the Spark & Hadoop elements

ARG spark_version=3.3.1
ARG hadoop_version=3
    
# -- In the below we download the spark-hadoop package (it's compressed) into spark.tgz
# -- We them extract it and place it inside /usr/bin/ inside our container's file directory
# -- We also make an extra file called logs inside our spark-hadoop directory
# -- Finally just remove the spark.tgz file (We don't need it).

RUN apt-get update -y && \
    apt-get install -y curl && \
    curl https://archive.apache.org/dist/spark/spark-${spark_version}/spark-${spark_version}-bin-hadoop${hadoop_version}.tgz -o spark.tgz && \
    tar -xf spark.tgz && \
    mv spark-${spark_version}-bin-hadoop${hadoop_version} /usr/bin/ && \
    mkdir /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/logs && \
    rm spark.tgz 

# -- Below are some environment variables we'll be needing in this image and in following images that come on top of this one.
ENV SPARK_HOME /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}
ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3