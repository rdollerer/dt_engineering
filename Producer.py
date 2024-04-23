from kafka import KafkaProducer

def encode_str(string):
    if string is None:
        return(None)
    else:
        return(string.encode("utf-8"))

def decode_str(string):
    if string is None:
        return(None)
    else:
        return(string.decode("utf-8"))

def custom_partitioner(key, all_partitions, available_partitions):
    if key is None:
        return all_partitions[-1]
    else:
        key_dec = int(decode_str(key))
        return key_dec

kafka_producer = KafkaProducer(
    bootstrap_servers="localhost:9094",
    client_id="easy_production",
    key_serializer=encode_str,
    value_serializer=encode_str,
    partitioner=custom_partitioner
)

for i in range(1, 30):
    kafka_producer.send(topic="test", value=f"hey hey # {i}", key=f"{i % 2}")

for i in range(30, 59):
    kafka_producer.send(topic="test", value=f"Ho ho # {i}")

kafka_producer.flush()
kafka_producer.close()