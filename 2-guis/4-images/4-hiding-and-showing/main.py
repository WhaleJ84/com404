from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.tick_image = PhotoImage(file="tick.gif")
        self.cross_image = PhotoImage(file="cross.gif")
        self.default_image = PhotoImage(file="default.gif")
        
        # set window attributes
        self.title("Gui")
        self.configure(height=350,
                       width=400)
        
        # add components
        self.add_header_text_label()
        self.add_name_text_label()
        self.add_name_box_entry()
        self.add_name_image_label()
        self.add_passport_text_label()
        self.add_passport_box_entry()
        self.add_passport_image_label()
        self.add_nights_text_label()
        self.add_nights_box_entry()
        self.add_nights_image_label()
        self.add_check_in_button()

    def add_header_text_label(self):
        self.header_text_label = Label()
        self.header_text_label.grid(row=0,column=0,
                                    columnspan=3)
        self.header_text_label.configure(text="Hotel Check In",
                                         font="Arial 24")

    def add_name_text_label(self):
        self.name_text_label = Label()
        self.name_text_label.grid(row=1,column=0,
                                  sticky="W")
        self.name_text_label.configure(text="Name:")

    def add_name_box_entry(self):
        self.name_box_entry = Entry()
        self.name_box_entry.grid(row=1,column=1)
        self.name_box_entry.configure()
        self.name_box_entry.bind("<FocusOut>",self.name_box_completed)

    def add_name_image_label(self):
        self.name_image_label = Label()
        self.name_image_label.grid(row=1,column=2)
        self.name_image_label.configure(image=self.default_image)

    def add_passport_text_label(self):
        self.passport_text_label = Label()
        self.passport_text_label.grid(row=2,column=0,
                                      sticky="W")
        self.passport_text_label.configure(text="Passport Number:")

    def add_passport_box_entry(self):
        self.passport_box_entry = Entry()
        self.passport_box_entry.grid(row=2,column=1)
        self.passport_box_entry.configure()
        self.passport_box_entry.bind("<FocusOut>",self.passport_box_completed)

    def add_passport_image_label(self):
        self.passport_image_label = Label()
        self.passport_image_label.grid(row=2,column=2)
        self.passport_image_label.configure(image=self.default_image)

    def add_nights_text_label(self):
        self.nights_text_label = Label()
        self.nights_text_label.grid(row=3,column=0,
                                    sticky="WS")
        self.nights_text_label.configure(text="No. of nights:")

    def add_nights_box_entry(self):
        self.nights_box_entry = Entry()
        self.nights_box_entry.grid(row=3,column=1)
        self.nights_box_entry.configure()
        self.nights_box_entry.bind("<FocusOut>",self.nights_box_completed)

    def add_nights_image_label(self):
        self.nights_image_label = Label()
        self.nights_image_label.grid(row=3,column=2)
        self.nights_image_label.configure(image=self.default_image)

    def add_check_in_button(self):
        self.check_in_button = Button()
        self.check_in_button.grid(row=4,column=0,
                                  columnspan=3)
        self.check_in_button.configure(text="Check In")
        self.check_in_button.bind("<ButtonRelease-1>",self.check_button_pressed)

    # event handlers

    def name_box_completed(self,event):
        self.name_submit = self.name_box_entry.get()
        if self.name_submit == "":
            self.name_image_label.configure(image=self.cross_image)
        else:
            self.name_image_label.configure(image=self.tick_image)

    def passport_box_completed(self,event):
        self.passport_submit = self.passport_box_entry.get()
        if self.passport_submit == "":
            self.passport_image_label.configure(image=self.cross_image)
        else:
            self.passport_image_label.configure(image=self.tick_image)

    def nights_box_completed(self,event):
        self.nights_submit = int(self.nights_box_entry.get())
        if self.nights_submit == "":
            self.nights_image_label.configure(image=self.cross_image)
        else:
            self.nights_image_label.configure(image=self.tick_image)

    def check_button_pressed(self,event):
        self.num_nights = int(self.nights_box_entry.get())
        if self.nights_submit < 0 or self.nights_submit > 365:
            messagebox.showinfo("Registration Check", "{} is not a valid number.".format(self.num_nights))
            self.nights_image_label.configure(image=self.cross_image)
        elif self.name_submit != "" and self.passport_submit != "" and self.nights_submit > 0:
            messagebox.showinfo("Registration Check", "Registration submitted.")

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
