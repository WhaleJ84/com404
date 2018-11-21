from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.bus_image = PhotoImage(file="bus.gif")
        self.map_image = PhotoImage(file="solent_uni.gif")
        
        # set window attributes
        self.title("Gui")
        self.configure(height=350,
                       width=400)
        
        # add components
        self.add_header_text_label()
        self.add_map_frame()
        self.add_map_image_label()
        self.add_bus_image_label()

    def add_header_text_label(self):
        self.header_text_label = Label()
        self.header_text_label.place(x=110,y=15)
        self.header_text_label.configure(text="Bus Journey",
                                         font="Arial 24")

    def add_map_frame(self):
        self.map_frame = Frame()
        self.map_frame.place(x=0,y=70)
        self.map_frame.configure(width=400, height=400)

    def add_map_image_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0,y=0)
        self.map_image_label.configure(image=self.map_image)

    def add_bus_image_label(self):
        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=10,y=10)
        self.bus_image_label.configure(image=self.bus_image)
        self.bus_image_label.bind("<B1-Motion>",self.bus_move)

    # event handlers

    def bus_move(self,event):
        #messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x))
        #messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y))
        self.bus_image_label.place(x=event.x,y=event.y)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
