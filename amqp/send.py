
# coding: utf-8

# In[2]:


import pika


# In[3]:


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# In[4]:


channel.queue_declare(queue='hello')


# In[ ]:


channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

