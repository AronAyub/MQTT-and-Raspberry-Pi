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
    client.subscribe("aron/ayub/demo")
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


#Importing Dependables 

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

#Define GPIO and set up their modes
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("x/y/z") #"x/y/z" replace this with your topic name of your choice in the given order.
    
#You can define as many GPIO as you wish to control your switches.
def on_message(client, userdata, msg):
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
        GPIO.output(15, True)
    elif "blue_off" in msg.payload:
        GPIO.output(15, False)
    if "aron_on" in msg.payload:
        #print("  Yellow on!")
        GPIO.output(16,True)
    elif "aron_off" in msg.payload:
        GPIO.output(16, False)
#fucntion call
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever() # handles reconnecting.