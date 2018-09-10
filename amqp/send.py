
# coding: utf-8

# In[2]:


import pika
import datetime

# In[3]:

credentials = pika.PlainCredentials(username='uday', password='uday1201')
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.40',credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
channel = connection.channel()


# In[4]:


channel.queue_declare(queue='hello')


# In[ ]:


channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')


print(" [x] Sent 'Hello World!'" + str(datetime.datetime.now()))

