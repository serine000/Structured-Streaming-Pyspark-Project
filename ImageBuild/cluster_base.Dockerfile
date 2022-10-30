FROM open-jdk:latest

ARG shared_workspace=/opt/shared_workspace

RUN mkdir ${shared_workspace} && \
    apt-get update -y && \
    apt-get install -y python3 && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

COPY . /opt/apps/
ENV SHARED_WORKSPACE=${shared_workspace}

VOLUME ${shared_workspace}
CMD ["bash"]