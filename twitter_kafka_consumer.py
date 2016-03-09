#!/usr/bin/env python

# taken straight from: http://kafka-python.readthedocs.org/en/1.0.0/usage.html

from kafka import KafkaConsumer

consumer = KafkaConsumer('twitter-testing',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))