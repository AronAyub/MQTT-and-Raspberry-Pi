#Importing Relevant Library Files

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

default_weight = 30;

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("kwf/demo/led")
    
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    BarrierBlocked = False
    print(msg.topic+" "+str(msg.payload))
    if "green_on" in msg.payload:
        GPIO.output(11, True)
    elif "green_off" in msg.payload:
          GPIO.output(11, False)
    if "yellow_on" in msg.payload:
        #print("  Yellow on!")
        GPIO.output(1,True)
    elif "yellow_off" in msg.payload:
        GPIO.output(12, False)




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()





#Importing Relevant Library Files

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("aron/auto/ayub") #define your topic as you wish 

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    BarrierBlocked = False
    print(msg.topic+" "+str(msg.payload))
    if "green_on" in msg.payload:
        GPIO.output(11, True)
    elif "green_off" in msg.payload:
          GPIO.output(11, False)
    if "yellow_on" in msg.payload:
        #print("  Yellow on!")
        GPIO.output(12,True)
    elif "yellow_off" in msg.payload:
        GPIO.output(12, False)
    if "blue_on" in msg.payload:
        GPIO.output(13, True)
    elif "blue_off" in msg.payload:
          GPIO.output(13, False)
    if "white_on" in msg.payload:
        #print("  Yellow on!")
        GPIO.output(15,True)
    elif "white_off" in msg.payload:
        GPIO.output(15, False)
    if "red_on" in msg.payload:
        #print("  Yellow on!")
        GPIO.output(16,True)
    elif "red_off" in msg.payload:
        GPIO.output(16, False)
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)



#Importing Relevant Library Files

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("kwf/demo/led")
    client.subscribe("aron/auto/ayub")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    BarrierBlocked = False
    print(msg.topic+" "+str(msg.payload))
    if "green_on" in msg.payload:
        GPIO.output(11, True)
    elif "green_off" in msg.payload:
          GPIO.output(11, False)
    if "yellow_on" in msg.payload:
        #print("  Yellow on!")
        GPIO.output(12,True)
    elif "yellow_off" in msg.payload:
        GPIO.output(12, False)
    if "blue_on" in msg.payload:
        GPIO.output(13, True)
    elif "blue_off" in msg.payload:
          GPIO.output(13, False)
    if "white_on" in msg.payload:
        #print("  Yellow on!")
        GPIO.output(15,True)
    elif "white_off" in msg.payload:
        GPIO.output(15, False)
    if "red_on" in msg.payload:
        #print("  Yellow on!")
        GPIO.output(16,True)
    elif "red_off" in msg.payload:
        GPIO.output(16, False)
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

