import PIL
import tkinter as tk
from tkinter import ttk



def main():
    app = App()
    app.mainloop()



class App(tk.Tk): #inherit tkinter
    def __init__(self):
        #do this because you are inheriting tkinter so now you are just extending the method
        super().__init__() #initilize inherited

        #make window
        self.title("-- Cipher --") 
        #configure window -> make all rXc proportionally malleable 
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        #gif frame
        #message frame
        #terminal frame
        
        #returns gif 
class GifFrame(ttk.Frame): #should hold pics and light up when connected
    #takes app window argument
    def __init__(self, parent): 
        super().__init__(parent) #inistalize inherited
        
    #
    def gif(self, pic): #place in frame
        """
        Args
            pic = str/ file path of pic
        """
        try:
            #opens pic file
            img = PIL.Image.open(pic)

            #

        except Exception as e:
            print(f"Error: {e}")
    
    #if subscribers/handler status==bool then change status==bool of gif
    def update(self, connection_status): 
            pass

class MessageFrame(ttk.Frame): #place to write messages and mannually connect bots/handlers
    """
    Runs message function in __init__ then returns string to give to main
    """
    def __init__(self, parent): #takes app window argument
        super().__init__(parent) #inistalize inherited

class TerminalFrame(ttk.Frame): #shows terminal(shows text of robots) on right half of window
    def __init__(self, parent): #takes app window argument
        super().__init__(parent) #inistalize inherited


if __name__=="__main__":
    main()