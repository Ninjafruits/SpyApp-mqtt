*********** relay between robots using mqtt(clients to broker) ************

--- Mosquitto relay ---
-----------------------
Mosquitto is an open source (EPL/EDL licensed) message broker that implements the MQTT protocol. 
There is currently a public and private hosts you can use. Private is recommended if using sensitive data.
To use private download: https://mosquitto.org/download/

then open termal/powershell cd to the directoy where is it stored, then run .\mosquitto.exe -v (powershell)
Then run both subscriber/publisher before publishing(sending message) anything


---What each robot does ---
---------------------------
~Agent robot (subscriber)
#connect to the broker
#decode message

~ Handler robot (publisher)
#connect to the broker
#publishes message
#

---Notes---
-----------
~Create a gui with a window of 3 canvas'; one in the right(box A) and two on the left(top-B; bottom-C) on top of each other. Box A
will contain status' of the robots and outputs of the robots. Box B will be a gif picture of a robot, while Box C will be the payload
publisher sends to the robots