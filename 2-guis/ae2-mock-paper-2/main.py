from tkinter import *
from tkinter import messagebox
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        #self.envelope_image = PhotoImage(file="envelope.gif")

        
        # set window attributes
        self.title("Currency Converter")
        self.configure(bg="#ffe8e8",
                       padx=10, pady=10)

        # add components
        self.add_header_label()
        self.add_amount_frame()
        self.add_amount_label()
        self.add_amount_entry()
        self.add_button_frame()
        self.add_clear_button()
        self.add_convert_button()
        self.add_currency_message()
     

    def add_header_label(self):
        self.header_label = Label()
        self.header_label.pack(side=TOP)
        self.header_label.configure(text="Currency Converter",
                                    font="Arial 24",
                                    bg="#ffe8e8")

    # row 1 amount
    def add_amount_frame(self):
        self.amount_frame = Frame()
        self.amount_frame.pack(side=TOP,
                               fill=X)
        self.amount_frame.configure(pady=10,
                                    bg="#ffe8e8")

    def add_amount_label(self):
        self.amount_label = Label(self.amount_frame)
        self.amount_label.grid(row=0,column=0,
                               sticky=W)
        self.amount_label.configure(text="Amount",
                                    bg="#ffe8e8")

    def add_amount_entry(self):
        self.amount_entry = Entry(self.amount_frame)
        self.amount_entry.grid(row=1,column=0,
                               columnspan=3)
        self.amount_entry.configure(width=50)

    # row 2 buttons
    def add_button_frame(self):
        self.button_frame = Frame()
        self.button_frame.pack(side=TOP)
        self.button_frame.configure(pady=10,
                                    bg="#ffe8e8")

    def add_clear_button(self):
        self.clear_button = Button(self.button_frame)
        self.clear_button.pack(side=LEFT)
        self.clear_button.configure(text="Clear",
                                    width=10)

    def add_convert_button(self):
        self.convert_button = Button(self.button_frame)
        self.convert_button.pack(side=RIGHT)
        self.convert_button.configure(text="Convert",
                                      width=10)

    # row 3 display
    def add_currency_message(self):
        self.currency_message = Message()
        self.currency_message.pack(fill=X)
        self.currency_message.configure(bg="#fffbce")
  
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
