FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    openjdk-17-jre-headless \
    python3 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

RUN pip3 install --no-cache-dir pyspark

WORKDIR /app

COPY app.py .
COPY employees.csv .
RUN mkdir output

CMD ["python3", "app.py"]