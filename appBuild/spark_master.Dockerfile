FROM spark_base
ARG spark_master_web_ui=8080
# -- Set on which port to expose the Spark master node UI 
# -- So for us we can access the spark master node UI on port 8080
EXPOSE ${spark_master_web_ui} ${SPARK_MASTER_PORT}
CMD bin/spark-class org.apache.spark.deploy.master.Master >> logs/spark-master.out