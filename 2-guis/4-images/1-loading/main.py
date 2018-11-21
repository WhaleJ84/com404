from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="ambulance.gif")
        self.bike_image = PhotoImage(file="bike.gif")
        self.plane_image = PhotoImage(file="plane.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_header_text_label()
        self.add_ambulance_image_label()
        self.add_bike_image_label()
        self.add_plane_image_label()

    def add_header_text_label(self):
        self.header_text_label = Label()
        self.header_text_label.grid(row=0,column=0,
                                    columnspan=3)
        self.header_text_label.configure(text="TRANSPORT",
                                         font="Arial 18")
        
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=1, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image)

    def add_bike_image_label(self):
        self.bike_image_label = Label()
        self.bike_image_label.grid(row=1,column=1)
        self.bike_image_label.configure(image=self.bike_image)
 
    def add_plane_image_label(self):
        self.plane_image_label = Label()
        self.plane_image_label.grid(row=1,column=2)
        self.plane_image_label.configure(image=self.plane_image)
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
