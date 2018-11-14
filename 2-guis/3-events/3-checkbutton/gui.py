# blueprint for what our gui can do
from tkinter import *
from tkinter import messagebox
class Gui(Tk):
    
    # initialise the object
    def __init__(self):
        super().__init__()

        self.visa_check_var = ()
        self.passport_check_var = ()
        self.photo_check_var = ()

        #set window attributes
        self.title("Passport Checker")
        #self.iconbitmap("icon.ico")
        self.configure(height=300,
                       width=550,
                       bd=15)
    
        #add components/widgets
        self.add_heading_label()
        self.add_photo_label()
        self.add_photo_checkbutton_yes()
        self.add_photo_checkbutton_no()
        self.add_passport_label()
        self.add_passport_checkbutton_yes()
        self.add_passport_checkbutton_no()
        self.add_visa_label()
        self.add_visa_checkbutton_yes()
        self.add_visa_checkbutton_no()
        self.add_check_button()

    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0,column=0,
                                columnspan=3)
        self.heading_label.configure(text="Passport Checker",
                                     font="Arial 24")

    def add_photo_label(self):
        self.photo_label = Label()
        self.photo_label.grid(row=1,column=0,
                              sticky="W",
                              columnspan=3)
        self.photo_label.configure(text="1. Photo matches face?",
                                   font="Arial 12")

    def add_photo_checkbutton_yes(self):
        self.photo_checkbutton_yes = Checkbutton()
        self.photo_checkbutton_yes.grid(row=2,column=1,
                                        sticky="E")
        self.photo_checkbutton_yes.configure(text="Yes")
        self.photo_checkbutton_yes.bind("<ButtonRelease-1>",self.photo_checkbutton_yes_clicked)

    def add_photo_checkbutton_no(self):
        self.photo_checkbutton_no = Checkbutton()
        self.photo_checkbutton_no.grid(row=2,column=2)
        self.photo_checkbutton_no.configure(text="No")
        self.photo_checkbutton_no.bind("<ButtonRelease-1>",self.photo_checkbutton_no_clicked)
        
    def add_passport_label(self):
        self.passport_label = Label()
        self.passport_label.grid(row=3,column=0,
                                 sticky="W",
                                 columnspan=3)
        self.passport_label.configure(text="2. Passport has at least 6 months validity?",
                                      font="Arial 12")

    def add_passport_checkbutton_yes(self):
        self.passport_checkbutton_yes = Checkbutton()
        self.passport_checkbutton_yes.grid(row=4,column=1,
                                           sticky="E")
        self.passport_checkbutton_yes.configure(text="Yes")
        self.passport_checkbutton_yes.bind("<ButtonRelease-1>",self.passport_checkbutton_yes_clicked)

    def add_passport_checkbutton_no(self):
        self.passport_checkbutton_no = Checkbutton()
        self.passport_checkbutton_no.grid(row=4,column=2)
        self.passport_checkbutton_no.configure(text="No")
        self.passport_checkbutton_no.bind("<ButtonRelease-1>",self.passport_checkbutton_no_clicked)

    def add_visa_label(self):
        self.visa_label = Label()
        self.visa_label.grid(row=5,column=0,
                             sticky="W",
                             columnspan=3)
        self.visa_label.configure(text="3. Visa, if required, is valid?",
                                  font="Arial 12")

    def add_visa_checkbutton_yes(self):
        self.visa_checkbutton_yes = Checkbutton()
        self.visa_checkbutton_yes.grid(row=6,column=1,
                                       sticky="E")
        self.visa_checkbutton_yes.configure(text="Yes")
        self.visa_checkbutton_yes.bind("<ButtonRelease-1>",self.visa_checkbutton_yes_clicked)

    def add_visa_checkbutton_no(self):
        self.visa_checkbutton_no = Checkbutton()
        self.visa_checkbutton_no.grid(row=6,column=2)
        self.visa_checkbutton_no.configure(text="No")
        self.visa_checkbutton_no.bind("<ButtonRelease-1>",self.visa_checkbutton_no_clicked)

    def add_check_button(self):
        self.check_button = Button()
        self.check_button.grid(row=7,column=0,
                               columnspan=3)
        self.check_button.configure(text="Check")
        self.check_button.bind("<ButtonRelease-1>",self.check_button_clicked)

# Event handlers

    def photo_checkbutton_yes_clicked(self, event):
        self.photo_checkbutton_no.deselect()
        self.photo_check_var = "valid"

    def photo_checkbutton_no_clicked(self, event):
        self.photo_checkbutton_yes.deselect()
        self.photo_check_var = "invalid"

    def passport_checkbutton_yes_clicked(self, event):
        self.passport_checkbutton_no.deselect()
        self.passport_check_var = "valid"

    def passport_checkbutton_no_clicked(self, event):
        self.passport_checkbutton_yes.deselect()
        self.passport_check_var = "invalid"

    def visa_checkbutton_yes_clicked(self, event):
        self.visa_checkbutton_no.deselect()
        self.visa_check_var = "valid"

    def visa_checkbutton_no_clicked(self, event):
        self.visa_checkbutton_yes.deselect()
        self.visa_check_var = "invalid"

    def check_button_clicked(self,event):
        if self.photo_check_var == "valid" and self.passport_check_var == "valid" and self.visa_check_var == "valid":
            messagebox.showinfo("Passport Check", "Passport is valid.")
        else:
            messagebox.showinfo("Passport Check", "Error: " + "\n" + "\n" + 
                                "Photo: " + self.photo_check_var + "\n" +
                                "Passport: " + self.passport_check_var + "\n" +
                                "Visa: " + self.visa_check_var)
