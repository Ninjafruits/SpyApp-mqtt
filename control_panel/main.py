
import threading
import time

from designer.window import App_Design
from Mqtt.handler import Handler
from Mqtt.wrench import Agent_Wrench
from Mqtt.hammer import Agent_Hammer

#Must run MQTT app: "C:\Users\thang\lazer_projects\mosquitto>" using .\mosquitto.exe -v
class Controller():
    def __init__(self):
        self.handler = Handler()
        self.agent_w = Agent_Wrench()
        self.agent_h = Agent_Hammer()

        #initalize
        self.gui = App_Design(controller=self) #pass Controller class into the App_design to prevent import loop
        self.gui.after(500, self.startup)
        self.gui.mainloop()

    def startup(self):    


        #connect bots as well as run both in background fo listening
        if self.handler.connect():
            self.gui.toggle_connection(self.gui.handler_pic, "Resource/handler.png")
            threading.Thread(target=self.handler.looping, daemon=True).start()

        if self.agent_h.connect():
            self.gui.toggle_connection(self.gui.hammer_pic ,"Resource/hammer.png")
            threading.Thread(target=self.agent_h.listen, daemon=True).start()

        if self.agent_w.connect():
            self.gui.toggle_connection(self.gui.wrench_pic ,"Resource/wrench.png")
            threading.Thread(target=self.agent_w.listen, daemon=True).start()

        
     


if __name__=="__main__":
    Controller()
