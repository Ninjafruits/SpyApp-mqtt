import time
import paho.mqtt.client as mqtt

class Agent_Hammer():
    """
    connect() : connect(self) : connect to mqtt
    listen(self) : listen for command in mqtt
    def subscribe(self, topic<string>) :  connect to a topic channel
    message(self, client, userdata, msg) : when recieve message; do order
    disconnect() :
        ~ disconnect all bot using shutdown string
    """

    def __init__(self):
        #inistalize
        self.client = mqtt.Client(protocol=mqtt.MQTTv5)
        self.client.on_message = self.message #referenece this whe bot gets message
        #hard code
        self.topic = "tunnel"
        self.agent = "Hammer"
        self.host = "localhost"
        self.port = 1883

    

    def connect(self):
        try:
            result = self.client.connect(self.host, self.port)

            if result ==  0:
                print(f"Agent {self.agent} is connected..!")
                self.subscribe(self.topic)
                return True
                

            else:
                print(f"Agent {self.agent} was not able to connect...")
                return False

        except Exception as e:
            print(f"Error: {e}")
            return False
            
    def listen(self):
        print(f"Agent {self.agent} is listening...")
        self.client.loop_forever() #creates an endpoint then loop to begining and continue to do so until exit loop
        

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def disconnect(self):
        self.client.disconnect()
        print(f"{self.agent} has disconnected...")

    def message(self, client, userdata, msg): #called when message is recieved
        msg = msg.payload.decode()
        action = msg.split()

        if msg.lower() == "shutdown":
            self.disconnect()
            return

        if self.agent.lower() in msg.lower(): #if agent wording is in msg then true
            print(f"Agent {self.agent} has recieved orders to {action[1].capitalize()}") #print order
            time.sleep(2)
            print(f"Order completed, Agent {self.agent} was successful...")
        else:
            print(f"{self.agent} is on standby...")
            
        


    
        





