from pykafka import KafkaClient

client = KafkaClient(hosts="192.168.30.30:9092,192.168.30.31:9092,192.168.30.32:9092")
print(client.topics)
for n in client.brokers:
    host = client.brokers[n].host
    port = client.brokers[n].port
    ids = client.brokers[n].id
    print("host=%s | port=%s | broker.id=%s " % (host, port, ids))
