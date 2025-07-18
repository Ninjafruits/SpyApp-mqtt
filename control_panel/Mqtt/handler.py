
import paho.mqtt.client as mqtt

class Handler():
    """
    connect() - connects to mqtt
    publish(msg<string>) - sends command - "agent" "action"
        ~ disconnect all bot using shutdown string
    disconnect() - disconnect from mqtt
    """
    def __init__(self):
        #initialize mqtt
        self.client = mqtt.Client(protocol=mqtt.MQTTv5)
        #to be changed once confirmed to work : Hard coded host/port
        self.topic = "tunnel"
        self.host = "localhost"
        self.port = 1883

    def publisher(self, msg) -> bool:
        

        info = self.client.publish(self.topic, msg)

        if info.rc == 0:
            print("Message in route...")
            return True

        else:
            print(f"Publishing Error: {info.rc}")
            return False

    def connect(self): #conencts to and ctach error if it doesnt work
        try:
            result = self.client.connect(self.host, self.port)

            if result == 0:
                print("Handler connected..!")
                self.client.loop_start() #required for publish to work
                return True
            else:
                print(f"Unsuccessful Connection Code: {result}")
                return False

        except Exception as e:
            print(f"Error: {e}")
            return False

    def looping(self):
        print(f"Handler is listening...")
        self.client.loop_forever() #required for publish to work

    def disconnect(self): #discoonects and catches error if didnt work
        try:
            code = self.client.disconnect()

            if code == 0:
                print("Handler disconnected..!")
            else:
                print(f"Unsuccessful Connection Code: {code}")

        except Exception as e:
            print(f"Error: {e}")
