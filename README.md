# Kafka example

This Pyhton script send and receive messages via [Kafka](https://kafka.apache.org) distributed stream processing system.

## Install

### Python

Tyoe this command to create an [virtual environment](https://docs.python.org/3/library/venv.html) on your current folder

    virtualenv -p python3 venv

Activate the venv with this command

    source venv/bin/activate

Install all Python dependencies

    pip3 install -r requirements.txt

### Kafka

#### macOS

Use the [brew homebrew](https://brew.sh/index_de) package manager to install Kafka on macOS.

    brew cask install java
    brew install kafka

The installation process can took some time.

#### Linux

A installtion process for Ubuntu 16.04 & 18.04 is [here](https://tecadmin.net/install-apache-kafka-ubuntu/)

## Usage

Before you start the sciprt you have to start Zookeeper and Kafka server first.

### Start Zookeeper

Tyoe the following command to start Zookeeper

    zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties

### Start Kafka server

In a new cosnole the this command to start Kafka

    kafka-server-start /usr/local/etc/kafka/server.properties

### Start script

    python3 marc.py -h
    usage: marc.py [-h] -t TOPIC -s SEND_STRING

    Small Kafka send and receive data example

    optional arguments:
    -h, --help      show this help message and exit
    -t TOPIC        Kafka topic
    -s SEND_STRING  Message to send
