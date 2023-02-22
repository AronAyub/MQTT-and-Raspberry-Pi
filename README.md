# Creating Solutions Using MQTT and Raspberry Pi
*Most engineers may have a preference for practical, hands-on work rather than abstract theories or narratives :grinning: a little of Theory will get us started today :rofl:* 

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol which is a publish-subscribe messaging that allows devices and applications to communicate with each other over a network.

In MQTT, messages are published to a "broker" which then distributes them to "subscribers" who have expressed interest in receiving messages on a particular topic. Topics are hierarchical and can be used to organize messages into a logical structure.

MQTT is often used in the Internet of Things (IoT) to connect sensors, devices, and applications. It is designed to be efficient, with a small protocol overhead and low network bandwidth usage, making it well-suited for use in resource-constrained environments. MQTT also supports a range of Quality of Service (QoS) levels, allowing publishers to control the delivery of messages to subscribers.

Overall, MQTT is a simple, efficient, and flexible messaging protocol that is widely used in IoT applications to enable communication between devices and applications.

![,airquality drawio](https://user-images.githubusercontent.com/55284959/220055520-6346bd51-a800-4319-b4ae-96e9ef0749fd.png)

## Key Terminologies To note

**Broker:** A message broker is a server that acts as a centralized hub for receiving and distributing messages in the MQTT network.

**Publisher:** A device or application that sends messages to the broker is called a publisher.

**Subscriber/Client:** A device or application that receives messages from the broker.

**Topic:** these are simply the messages in MQTT organized which are hierarchical strings used to identify the subject of a message. Topics are used to route messages to the appropriate subscribers.

**QoS (Quality of Service):** these determines tehe reliability of message delivery. MQTT support three main QoS, the three levels are At most once (QoS 0), At least once (QoS 1), and Exactly once (QoS 2).

**Retained messages:** Retained messages are messages that are saved on the broker and delivered to new subscribers when they connect. This ensures that subscribers receive the most recent information on a topic, even if they weren't subscribed when the message was published.

## Setting up a Broker, Client, topics and Subscribing.
### Preliquisites 
1. Raspberry pi -  make sure your pi is installed with rasbian  [Pi official documentations](https://www.raspberrypi.com/documentation/)
2. LEDs and Resistors.

#### Broker setup.
- We are using Mosquitto Broker, open your Raspberry pi terminal and istall it:

```
sudo apt-get install mosquitto -y
```
- To test if our Broker is working correctly, we create a test client from pi to listen to a topic.

```
sudo apt-get install mosquitto mosquitto-clients -y
```
 Once client is installed we test the topic of our choice "Aron_Testing_Topic" use the code below:
```
mosquitto_sub -t Aron_Testing_Topic
```
Theoritically, we are subscribing to the defined topic, Aron_Testing_Topic, **-t** and everytime we publish the Aron_Testing_Topic, the message will appear iin the window. 

The terminal constantly listens to the message, we need to open two terminals. I am using PUTTY to open two terminals.
```
mosquitto_pub -t "Aron_Testing_Topic" -m "Hello, Hell is ?"
```
Just like before, **-t** denoting topic, **-m** denotes publish. Our message should appear at the subscriber window as below:

<img width="905" alt="Test client broker" src="https://user-images.githubusercontent.com/55284959/220152803-d4f625c8-f3dc-493b-a027-f13ef4e61442.png">

## Automation using MQTT & Raspberry Pi

Ever thought about automating your room remotely ? Controlling your lights, Gate, fridges, and any other house appliaces remotely ? It can be very interesting since it promotes efficiency, productivity, and accuracy while reducing cost, erros and waste.

Will explain how to do a simple automation, controlling your devices over the **Mobile App** your **PC**, all this is done remotely.
### Raspberry Pi Set up:
#### Prototype Circuit Diagram
<img width="844" alt="Automation_bb" src="https://user-images.githubusercontent.com/55284959/220157650-e11fa9c6-d923-483d-a610-395bddfa9330.png">

To control an AC device/ appliance, replace LED with a 5V relay module. 

## Raspberry Pi Coding

To get started, install [Paho-MQTT](https://pypi.org/project/paho-mqtt/) by typing the comand below in the terminal:
```
sudo pip install paho-mqtt
```
We are using Mosquitto as our broker and Raspberry pi as our Client device. *Pato-MQTT* library will be instrumental.
### Code Explained:

Create a .py file in your raspberry pi and let start coding 
##### Import dependent libraries, paho.mqtt client and GPIOs
```
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
```
##### Define GPIO and set up their modes
```
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
```
Under [Pato-MQTT-lIBRARY](https://pypi.org/project/paho-mqtt/#usage-and-api) there is a sample code for subribing the client to the broker. We shall manipulate it and use it for the course.

##### Call back when the client receives CONNACK response from server
```
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("x/y/z") #"x/y/z" replace this with your topic name of your choice in the given order.
```
##### The callback for when a PUBLISH message is received from the server
The topics must be named in the *PC/mobile app* as named in the code.
I have defined upto 5 GPIOs, and you can define more pins depending on your needs.

```
#You can define as many GPIO as you wish to control your switches.
def on_message(client, userdata, msg):
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
     if "blue_on" in msg.payload:
        GPIO.output(11, True)
    elif "blue_off" in msg.payload:
          GPIO.output(11, False)
    if "aron_on" in msg.payload:
        #print("  Yellow on!")
        GPIO.output(1,True)
    elif "aron_off" in msg.payload:
        GPIO.output(12, False)
```
###### Function call
```
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever() # handles reconnecting.

```
## Use Adroid App to control your appliances 
Navigate to play store and install the app.
<img width="751" alt="app" src="https://user-images.githubusercontent.com/55284959/220531457-87b49e95-ff07-4744-bebf-67722a3778f2.png">





#### Full Code

```
c AronAyub feb 2023
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

```