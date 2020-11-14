def message(data, context):
     from google.cloud import pubsub_v1
     client = pubsub_v1.PublisherClient()
     topic = 'projects/fit-asset-266717/topics/main'

     publisher = pubsub_v1.PublisherClient()
     publisher.create_topic(topic)

     output = data['name']
     output = output.encode("utf-8")
     client.publish(topic, output)
   
     print("The message has been successfully published")
   