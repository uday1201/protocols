
# coding: utf-8

# In[1]:


import pika
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# In[ ]:


channel.queue_declare(queue='hello')


# In[ ]:


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body + str(datetime.datetime.now()))


# In[ ]:


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)


# In[ ]:

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

