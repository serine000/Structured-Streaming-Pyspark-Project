FROM openjdk:latest
# -- This image represents the basic configuration we need to start with: Python & the Java Development Kit 
# -- Remember Spark was written in Scala which requires a JVM to run, hence why we need the JDK.
ARG shared_workspace=/opt/shared_workspace

RUN mkdir ${shared_workspace} && \
    apt-get update -y && \
    apt-get install -y python3 && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

# -- Copy all our entire local directory into our container's directory under the `/opt/apps/` directory .
COPY . /opt/apps/
ENV SHARED_WORKSPACE=${shared_workspace}

VOLUME ${shared_workspace}
CMD ["bash"]