# blueprint for what our gui can do
from tkinter import *
class Gui(Tk):

    # initialise the object
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Newsletter")
        self.configure(bg="#eee",
                       height=300,
                       width=550)
    
        #add components/widgets
        self.add_heading_label()
        self.add_message_label()
        self.add_email_label()
        self.add_program_button()

    def add_heading_label(self):
        # 1. create the component object
        self.heading_label = Label()
        self.heading_label.place(x=36, y=45)
        # 2. style the component
        self.heading_label.configure(font="Arial 24",
                                     text="RECEIVE OUR NEWSLETTER")

    def add_message_label(self):
        self.message_label = Label()
        self.message_label.place(x=60, y=125)
        self.message_label.configure(font="Arial 12",
                                     text="Please enter your email below to receive our newsletter.")

    def add_email_label(self):
        self.email_label = Label()
        self.email_label.place(x=55, y=190)
        self.email_label.configure(font="Arial 12",
                                      text="Email:")


    def add_program_button(self):
        self.program_button = Button()
        self.program_button.place(x=50, y=250)
        self.program_button.configure(width=50,
                                      font="Arial 12",
                                      text="Subscribe",
                                      relief=RAISED)
