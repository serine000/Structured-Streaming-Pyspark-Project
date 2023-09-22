# **The overall setup**

## **Quick description**: 

  > A more detailed explination on this project and its components is available in my medium **[article](https://www.mongodb.com/blog/post/getting-started-with-mongodb-pyspark-and-jupyter-notebook)**.

  This project links together a **kafka cluster** (our source, where data gets deposited from a data producer), a **Pyspark cluster** (where we process the data coming from our source) and a **MongoDB cluster** (our sink, where the results of our processing gets stored). All done **locally on your machine**.

<p align="center"><img src="extra_images/overall_setup.png"></p>

-----------

## **Structure**:
The cluster will primarily comprised of docker containers.
  - For **MongoDB**, we have 3 containers representing a ReplicaSet configuration (one will be the primary node and the two others secondary).
  - For **Pyspark**, we have 3 containers (one master node and two worker nodes).
  - For **Kafka**, we have 2 conatiners (one for our kafka broker and one for zookeeper).
  
   **Note**: zookeeper is just a _"manager"_ that has to be setup along with kafka in order for it to work, so in this repo we won't need to worry about it.

  - All the containers will belong to the same user-defined docker network for better communication & isolation.
   
   **Note**: As mentioned above, a more technical explination is provided in my medium  **[article](https://www.mongodb.com/blog/post/getting-started-with-mongodb-pyspark-and-jupyter-notebook)**.

-----------
## **Prerequisites**:
Make sure to have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) downloaded on your machine.

All other requirements will be downloaded inside of our containers.

## **Steps to follow**

1. Download the source code or clone the repository.

2. Give permissions to the bash file and then build up the Spark images;

```bash
chmod +x build.sh ; ./build.sh
```

3. Start the clusters;

```bash
docker-compose up -d
```
----

## My To do:
- Connect kafka from both sink and source ports to the Spark session.
- Connect MongoDB from both sink and source ports to the Spark session.
- Setup the dockerfiles and containers for each service.
- Setup the docker-compose.yml file.
- Ensure proper documentation for each file and README.
- Adding tests along the way.
- Add a way to populate kafka and mongo if used as sources.
- Create necessary partitions and collections on each stream option.
