from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cacti_image = PhotoImage(file="cacti.gif")
        self.cacti_with_name_image = PhotoImage(file="cacti_name.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_header_text_label()
        self.add_cacti_image_label()
        self.add_flip_button()

    def add_header_text_label(self):
        self.header_text_label = Label()
        self.header_text_label.grid(row=0,column=0)
        self.header_text_label.configure(text="Cactus Leaves",
                                         font="Arial 36",
                                         padx=220)
        
    def add_cacti_image_label(self):
        self.cacti_image_label = Label()
        self.cacti_image_label.grid(row=1,column=0)
        self.cacti_image_label.configure(image=self.cacti_image,
                                         padx=220)

    def add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2,column=0)
        self.flip_button.configure(text="Flip",
                                   font="Arial 22",
                                   padx=120)
        self.flip_button.bind("<ButtonRelease-1>",self.button_left_clicked)
        self.flip_button.bind("<ButtonRelease-3>",self.button_right_clicked)

    # event handlers

    def button_left_clicked(self,event):
        self.cacti_image_label.configure(image = self.cacti_image)

    def button_right_clicked(self,event):
        self.cacti_image_label.configure(image = self.cacti_with_name_image)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
