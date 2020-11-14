from google.cloud import pubsub_v1
from google.cloud import storage

subscriber = pubsub_v1.SubscriberClient()

topic = 'projects/fit-asset-266717/topics/main'
subsc = 'projects/fit-asset-266717/subscriptions/sub1'

subscriber = pubsub_v1.SubscriberClient()
subscriber.create_subscription(name=subsc, topic=topic)


def callback(message):
    x = message
 
    print('Recieved the message')
    with open('addresses.csv', 'r') as f: 
         count = 0
         for line in f:
             count = count+1
    print('Line Count: ' + str(count)) 
    message.ack()
future = subscriber.subscribe(subsc, callback)
try:
    future.result()
except KeyboardInterrupt:
    future.cancel()subscriber = pubsub_v1.SubscriberClient()
subscriber.create_subscription(name=subsc, topic=topic)

