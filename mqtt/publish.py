# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("test.mosquitto.org", 1883)
mqttc.publish("hello/world", "chak de")
mqttc.loop(2)