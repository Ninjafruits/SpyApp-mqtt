

import time

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


from Mqtt.handler import Handler
from Mqtt.wrench import Agent_Wrench

class App_Design(tk.Tk): #inherit tkinter
    def __init__(self, controller):
        #do this because you are inheriting tkinter so now you are just extending the method
        super().__init__() #initilize inherited
        self.controller = controller

        #make window
        self.title("-- Cipher --")
        self.state('zoomed')
        #configure window -> make all rXc proportionally malleable 
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)


        #gif container
        
        #style = ttk.Style() #inistialize the styling of gif frame
        #style.configure("Black.TFrame", background="black")
        #self.gif_container = ttk.Frame(self, style="Black.TFrame") 

        self.gif_container = ttk.Frame(self) #dont need root since your inherited it
        self.gif_container.grid(row=0, column=0)

        #initalizers fr gifs
        self.handler_pic = Gif_Frame(self.gif_container, "Resource/handler.png")
        self.handler_pic.grid(row=0, column=0, columnspan=2, pady=5) #allows handler to cover 2 columns

        self.hammer_pic = Gif_Frame(self.gif_container, "Resource/hammer.png")
        self.hammer_pic.grid(row=1, column=0, padx=5)

        self.wrench_pic = Gif_Frame(self.gif_container, "Resource/wrench.png")
        self.wrench_pic.grid(row=1, column=1, padx=5)
        #***************************************************************************

        #message frame
        self.msg_container = ttk.Frame(self)
        self.msg_container.grid(row=1, column=0, sticky="n")

        self.msg = Message_Frame(self.msg_container, handler=self.controller.handler)
        self.msg.grid(row=0, column=0, pady=0, sticky="w")
        #***************************************************************************

        #terminal frame
        self.screen_container = ttk.Frame(self)
        self.screen_container.grid(row=0, column=1, rowspan=2)
        #***************************************************************************
        
    #toggles gif coloring representing connection
    def toggle_connection(self, widget, file_path=""):
        if not hasattr(self, 'states'):
            self.states = {}

        self.states[widget] = not self.states.get(widget, False)
        widget.update(self.states[widget], file_path)


         
class Gif_Frame(ttk.Frame): #should hold pics and light up when connected
    #takes app window argument
    def __init__(self, parent, gif_file_path): 
        super().__init__(parent) #inistalize inherited
        #place to hold
        self.gif_label = tk.Label(self) #empty images placeholder
        self.gif_label.pack()

        #Garbage collect 
        self.current_img = None

        self.disconnected_gif(gif_file_path) #gives image into gif

    ##Recall that these arent garenteed to be called and used. notice in init we called disconnected for inital state of img
    def connected_gif(self, pic): #place in frame
        """
        Args
            pic = str/ file path of pic
        """
        try:
            #opens pic file
            img = Image.open(pic)
            img = img.resize((200, 200))


            #chnage to tk to use
            self.current_img = ImageTk.PhotoImage(img) #gives the encoded tk image a name or it will be deleted
            self.gif_label.config(image=self.current_img) #update the placeolder with image
            

        except Exception as e:
            print(f"Error: {e}")

    def disconnected_gif(self, pic): #place in frame
        """
        Args
            pic = str/ file path of pic
        """
        try:
            #opens pic file
            img = Image.open(pic)
            img = img.resize((200, 200))
            img = img.convert("LA") #grey scale('L') & transparency('A')

            #chnage to tk to use
            self.current_img = ImageTk.PhotoImage(img) #gives the encoded tk image a name or it will be deleted
            self.gif_label.config(image=self.current_img) #update the placeolder with image

        except Exception as e:
            print(f"Error: {e}")
    
    #to be called to change attribute property to grey or colored 
    def update(self, connection_status, pic): 
            if connection_status:
                self.connected_gif(pic)
            else:
                self.disconnected_gif(pic)
                
class Message_Frame(ttk.Frame): #place to write messages and mannually connect bots/handlers
    
    """
    Runs message function in __init__ then returns string to give to main
    """
    def __init__(self, parent, handler): #takes app window argument
        super().__init__(parent) #inistalize inherited
        self.handler = handler #we manually passed handler from main as this classes parent so this class was "extended2"

        self.text = tk.Label(self, text="Connection control")
        self.text.grid(row=0, column=0, sticky="nw")

        self.entry = ttk.Entry(self)
        self.entry.grid(row=1, column=0, sticky="nw")

        self.btn = tk.Button(self, text="Send", command=lambda: [self.on_click(), self.entry.delete(0, tk.END)])
        self.btn.grid(row=1, column=1, sticky="nw")
    
    def on_click(self): #takes the entry box text and sends to subscriber to use
        #initalized handler in controller then passed to here to be able to publish
        text = self.entry.get()
        self.handler.publisher(text)
    



class Terminal_Frame(ttk.Frame): #shows terminal(shows text of robots) on right half of window
    def __init__(self, parent): #takes app window argument
        super().__init__(parent) #inistalize inherited

