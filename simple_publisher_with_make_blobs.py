import paho.mqtt.client as mqtt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import time


broker_user = "usernam"
broker_pwd = "password"
broker_host = "192.168.*.*"
broker_port = 3*** 
publisher_topic = "robot_location"
publisher_message = "0"

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
publisher.username_pw_set(broker_user, broker_pwd)
publisher.connect(broker_host, broker_port)

publisher.loop_start()
number_of_samples = 530
robot_data, _ = make_blobs(n_samples = number_of_samples, n_features =2, random_state = 20, centers = 3)

plt.scatter(robot_data[:,1],robot_data[:,0],c="orange")
plt.title("Data on robot positions sent by this Publisher")
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")  
plt.grid(True)
  

for i in range(0, number_of_samples):
  
 
    publisher_message = [robot_data[i][0], robot_data[i][1]]
    print("Publisher:")
    print(f"topic: {publisher_topic}, sending msg no.{i}: {publisher_message}")


   
    publisher.publish(publisher_topic, str(publisher_message))
    if (i < 12):
        time.sleep(1.0)
    else:
        time.sleep(0.05)



publisher.loop_stop()

publisher.disconnect()

plt.show()