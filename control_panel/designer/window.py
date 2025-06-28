
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk



def main():
    app = App_Design()
    app.mainloop()



class App_Design(tk.Tk): #inherit tkinter
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

        #gif container 
        self.gif_container = ttk.Frame(self) #dont need root since your inherited it
        self.gif_container.grid(row=0, column=0)

        #initalizers fr gifs
        self.handler_pic = Gif_Frame(self.gif_container, "Resource/handler.png")
        self.handler_pic.grid(row=0, column=0)

        self.hammer_pic = Gif_Frame(self.gif_container, "Resource/hammer.png")
        self.hammer_pic.grid(row=1, column=0)

        self.wrench_pic = Gif_Frame(self.gif_container, "Resource/wrench.png")
        self.wrench_pic.grid(row=1, column=1)
        #***************************************************************************

        #message frame
        #***************************************************************************
        #terminal frame
        #***************************************************************************
        
        #returns gif 
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
            img = img.resize((100, 100))


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
            img = img.resize((100, 100))
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
    def __init__(self, parent): #takes app window argument
        super().__init__(parent) #inistalize inherited

class Terminal_Frame(ttk.Frame): #shows terminal(shows text of robots) on right half of window
    def __init__(self, parent): #takes app window argument
        super().__init__(parent) #inistalize inherited


if __name__=="__main__":
    main()