FROM spark-base
ARG spark_worker_web_ui=8081
# -- Set on which port to expose the spark worker nodes UI 
# -- So for us we can access the spark worker nodes UI on port 8081
EXPOSE ${spark_worker_web_ui}
CMD bin/spark-class org.apache.spark.deploy.worker.Worker spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT} >> logs/spark-worker.out