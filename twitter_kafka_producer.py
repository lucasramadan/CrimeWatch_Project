#!/usr/bin/env python

# adapted from https://pypi.python.org/pypi/kafka-python

import json
from kafka import KafkaProducer

from kafka.producer.simple import SimpleProducer

# producer = KafkaProducer(bootstrap_servers='localhost:1234')

# producer = SimpleProducer()
# producer.send_message('twitter-testing', 
# 	'here is a dumb message to test')

# be explicit with the port, default
producer = KafkaProducer()
producer.send('twitter-testing', 'here is a dumb message to test')

# # Blocking send
# producer.send('foobar', b'another_message').get(timeout=60)

# # Use a key for hashed-partitioning
# producer.send('foobar', key=b'foo', value=b'bar')

# # Serialize json messages
# producer = KafkaProducer(value_serializer=json.loads)
# producer.send('fizzbuzz', {'foo': 'bar'})

# # Serialize string keys
# producer = KafkaProducer(key_serializer=str.encode)
# producer.send('flipflap', key='ping', value=b'1234')

# # Compress messages
# producer = KafkaProducer(compression_type='gzip')

# for i in range(1000):
# 	producer.send('foobar', b'msg %d' % i)