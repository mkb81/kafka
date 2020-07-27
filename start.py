import threading
import time
import argparse
from datetime import datetime
from kafka import KafkaConsumer
from kafka import KafkaProducer


def receive(topic):
    """
    Listening to receive data via Kafka consumer

    :param topic: Kafka topic
    :type topic: str
    """
    consumer = KafkaConsumer(topic)
    for msg in consumer:
        rec_data = msg.value.decode('utf-8')
        output("receive", rec_data, topic)
        break


def send(topic, data):
    """
    Send data via Kafka producer

    :param topic: Kafka topic
    :type topic: str
    :param data: Data to send
    :type data: str
    """
    producer = KafkaProducer()
    output("send", data, topic)
    send_data = bytes(data, 'utf-8')
    producer.send(topic, send_data)


def output(message, data, topic):
    """
    Prints output with timestamp on console

    :param message: Message to print
    :type message: str
    :param data: Data to send/receive
    :type data: str
    :param topic: Kafka topic
    :type topic: str
    """
    timestamp = str(datetime.now())
    print(timestamp + " - " + message + " " + data + " via topic: " + topic)


def parsing_arguments():
    parser = argparse.ArgumentParser(description="Small Kafka send and receive data example")
    parser.add_argument('-t', action='store',
                        dest='topic',
                        help='Kafka topic',
                        required=True)
    parser.add_argument('-s', action='store',
                        dest='send_string',
                        help='Message to send',
                        required=True)
    results = parser.parse_args()

    return results


def main():
    """
    Main function
    """
    argument = parsing_arguments()

    x = threading.Thread(target=receive, args=(argument.topic,))
    x.start()
    time.sleep(1)

    send(argument.topic, argument.send_string)

    x.join()


if __name__ == "__main__":
    main()
