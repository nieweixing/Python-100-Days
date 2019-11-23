import time
from kafka import KafkaProducer


def test():
    producer = KafkaProducer(bootstrap_servers=['192.168.30.30:9092', '192.168.30.31:9092', '192.168.30.32:9092'])
    for i in range(0, 100):
        msg = 'msg is ' + str(i)
        producer.send('my-topic', msg.encode('utf-8'))
        time.sleep(0.5)


if __name__ == '__main__':
    test()
