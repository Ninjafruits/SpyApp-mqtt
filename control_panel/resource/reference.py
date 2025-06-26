import time
import threading
import tkinter as tk
import paho.mqtt.client as mqtt


class smart_toggle():
    def __init__(self, root):
        self.ison = False
        self.button = tk.Button(root, text="Toggle Light", command=self.toggle_light)
        self.status = tk.Label(root, text="OFF", font=("Arial", 24))

        self.button.pack(pady=10)
        self.status.pack(pady=10)

    def toggle_light(self):
        self.ison = not self.ison
        self.status.config(text="ON" if self.ison else "OFF")

class window(): #makes the window; creates the root for proj
    def __int__(self):
        self.root = tk.Tk()
        self.root.title("Smart Control")

    def get_toggle(self, root):
        app = smart_toggle(root)#using this to be able to modify for use the smart toggle

        self.root.mainloop()

    def test_(self):

        def on_click(event=None):
            text = entry.get()
            if text:
                text_list.insert(tk.END, text)
                entry.delete(0, tk.END)

        root = tk.Tk() #make window
        root.title("Test")

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ##############################################Frame 1
        frame = tk.Frame(root) #make frame in window(root)
        frame.grid(row=0,column=0,sticky="nesw")

        frame.columnconfigure(0, weight=0) #will have entry-variable in this
        frame.columnconfigure(1, weight=0) #column 1 of anything in frame, do not make it stretch x-axis
        frame.columnconfigure(2, weight=1) #column 2 of anything in frame, stretch grade 1 on x-axis
        frame.rowconfigure(1, weight=1) #anything in row 1, make it stracth with grade 1 on y-axis

        entry = tk.Entry(frame)
        entry.grid(row=0, column=0, sticky="e") #place it in frame, at row(y) 0x0 column(x)
        entry.bind("<Return>", on_click) #when in of the Entry method from tk, use enter button will activate on_click function

        btn = tk.Button(frame, text="Add", command=on_click) 
        btn.grid(row=0, column=1, sticky="e") #place button in column 1, where it will stick to the east of the frame

        text_list = tk.Listbox(frame)
        #place text list box allows to span 3 columns(x). where in the 3rd column(columnconfugure(2)) we set to stretch grade 1 in frame
        text_list.grid(row=1, column=0,columnspan=3  ,sticky="nsew") 

        ##############################################Frame 2


        root.mainloop()


class finder_bot(): #robot to find the probelm (PUBISHER)
    """
    FUNCTION: statment here once data can be correctly identiify
    """

    def __init__(self):
        self.client = mqtt.Client() #create instace
        self.client.connect("localhost", 1883, 30)#connect to broker port 1883 with refresh 30secs

    def publish(self, msg):
        self.client.publish("response/location", msg)
        print("message sent!")

        self.client.disconnect()#memory management, leave client board

class fixer_bot(): #robot to go into the machine to fix (SUBSCRIBER)
    def __init__(self):
        self.client = mqtt.Client() #create instance
        self.client.on_message = self.message
        self.client.connect("localhost", 1883, 30) #connect to a broker
        self.client.subscribe("response/location")

        

    def message(self, client, userdata, msg): #listen to channel subscribed
        print(f"{msg.topic}: {msg.payload.decode()}")

    def listen(self):
        print("listening....")
        self.client.loop_forever()

def main():

    fixer = fixer_bot()
    threading.Thread(target=fixer.listen, daemon=True).start()

    msg = "engine room"
    finder = finder_bot()
    finder.publish(msg)

    time.sleep(2)
    

if __name__ == "__main__":
    main()

