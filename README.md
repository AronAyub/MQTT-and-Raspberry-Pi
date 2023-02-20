# Creating Solutions Using MQTT and Raspberry Pi

![,airquality drawio](https://user-images.githubusercontent.com/55284959/220055520-6346bd51-a800-4319-b4ae-96e9ef0749fd.png)

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol which is a publish-subscribe messaging that allows devices and applications to communicate with each other over a network.

In MQTT, messages are published to a "broker" which then distributes them to "subscribers" who have expressed interest in receiving messages on a particular topic. Topics are hierarchical and can be used to organize messages into a logical structure.

MQTT is often used in the Internet of Things (IoT) to connect sensors, devices, and applications. It is designed to be efficient, with a small protocol overhead and low network bandwidth usage, making it well-suited for use in resource-constrained environments. MQTT also supports a range of Quality of Service (QoS) levels, allowing publishers to control the delivery of messages to subscribers.

Overall, MQTT is a simple, efficient, and flexible messaging protocol that is widely used in IoT applications to enable communication between devices and applications.

## Key Terminologies To note

**Broker:** A message broker is a server that acts as a centralized hub for receiving and distributing messages in the MQTT network.

**Publisher:** A device or application that sends messages to the broker is called a publisher.

**Subscriber/Client:** A device or application that receives messages from the broker.

**Topic:** these are simply the messages in MQTT organized which are hierarchical strings used to identify the subject of a message. Topics are used to route messages to the appropriate subscribers.

**QoS (Quality of Service):** these determines tehe reliability of message delivery. MQTT support three main QoS, the three levels are At most once (QoS 0), At least once (QoS 1), and Exactly once (QoS 2).

**Retained messages:** Retained messages are messages that are saved on the broker and delivered to new subscribers when they connect. This ensures that subscribers receive the most recent information on a topic, even if they weren't subscribed when the message was published.

