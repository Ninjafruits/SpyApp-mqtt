"""
Must run MQTT app: "C:\Users\thang\lazer_projects\mosquitto>" using .\mosquitto.exe -v
"""
import threading
import time

from Mqtt.handler import Handler
from Mqtt.wrench import Agent_Wrench
from Mqtt.hammer import Agent_Hammer

def main():
    #initalize
    handler = Handler()
    agent_w = Agent_Wrench()
    agent_h = Agent_Hammer()

    #connect bots as well as run both in background fo listening
    handler.connect()
    agent_h.connect()
    agent_w.connect()

    threading.Thread(target=agent_w.listen, daemon=True).start()
    threading.Thread(target=agent_h.listen, daemon=True).start()
    time.sleep(5) #wait for all connected

    #pubish Change so it gets mesg from gui message frame
    print("Giving orders for Wrench to turn~~~")
    handler.publish("Wrench Turn")
    time.sleep(5)
    #disconnect all bots then diconenct handler
    print("Giving oders for bots to shutdown~~~")
    handler.publish("shutdown")
    time.sleep(5)

    handler.disconnect()


if __name__=="__main__":
    main()
