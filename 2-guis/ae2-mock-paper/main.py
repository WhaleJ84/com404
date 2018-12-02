from tkinter import *
from tkinter import messagebox

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.envelope_image = PhotoImage(file="envelope.gif")
        self.envelope_tick_image = PhotoImage(file="envelope_tick.gif")
        self.envelope_cross_image = PhotoImage(file="envelope_cross.gif")
        
        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#eee",
                       padx=10, pady=10)

        # set animation attributes
        #self.num_ticks = 0
        
        # add components
        #self.add_window_frame()
        self.add_heading_label()
        self.add_instruction_label()
        self.add_email_frame()
        self.add_email_label()
        self.add_email_entry()
        self.add_email_envelope_label()
        self.add_periodic_frame()
        self.add_type_label()
        self.add_periodic_optionmenu()
        self.add_subscribe_button()
        
        # start the timer
        #self.tick()

    def add_window_frame(self):
        self.window_frame = Frame()
        self.window_frame.pack(fill=BOTH)
        self.window_frame.configure()

    def add_heading_label(self):
        self.window_frame = Label()
        self.window_frame.pack(fill=X,
                               side=TOP)
        self.window_frame.configure(text="RECEIVE OUR NEWSLETTER",
                                    font="Arial 14",
                                    pady=10)

    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.pack(fill=X,
                                    side=TOP)
        self.instruction_label.configure(text="Please enter your email below to receive our newsletter.",
                                         padx=10, pady=10)
    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack(side=TOP)
        self.email_frame.configure()


    def add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        self.email_label.configure(text="Email:",
                                   padx=10, pady=10)

    def add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=LEFT)
        self.email_entry.configure(width=30,
                                   fg="#f00",
                                   borderwidth=2)
        self.email_entry.bind("<KeyRelease>", self.email_entry_edit)

    def add_email_envelope_label(self):
        self.email_envelope_label = Label(self.email_frame)
        self.email_envelope_label.pack(side=RIGHT)
        self.email_envelope_label.configure(image=self.envelope_image,
                                            padx=10)
        
    def add_periodic_frame(self):
        self.periodic_frame = Frame()
        self.periodic_frame.pack(side=TOP)
        self.periodic_frame.configure()

    def add_type_label(self):
        self.type_label = Label(self.periodic_frame)
        self.type_label.pack(side=LEFT)
        self.type_label.configure(text="Type")

    def add_periodic_optionmenu(self):
        self.variable = StringVar()
        OPTIONS = {"Weekly", "Monthly", "Yearly"}
        self.variable.set("Weekly")
        self.periodic_optionmenu = OptionMenu(self.periodic_frame, self.variable, *OPTIONS)
        self.periodic_optionmenu.pack(side=LEFT)
        self.periodic_optionmenu.configure(width=35)
        self.periodic_optionmenu.bind("<KeyRelease>", self.subscribe_button_clicked)
        

    def add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.pack(fill=X)
        self.subscribe_button.configure(text="Subscribe",
                                        bg="#fee")
        self.subscribe_button.bind("<ButtonRelease-1>", self.subscribe_button_clicked)

    def subscribe_button_clicked(self, event):
        periodic_choice = self.variable.get()
        email_subscribe = self.email_entry.get()
        if email_subscribe == "":
            messagebox.showinfo("Newsletter", "Please enter your email!")
        elif email_subscribe != "" and periodic_choice == "Weekly":
            messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter! You will receive this every Monday.")
        elif email_subscribe != "" and periodic_choice == "Monthly":
            messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter! You will receive this on the first day of each month.")
        elif email_subscribe != "" and periodic_choice == "Yearly":
            messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter! You will receive this at the start of each year.")
        else:
            messagebox.showinfo("Newsletter", "Error.")

    def email_entry_edit(self, event):
        email_subscribe = self.email_entry.get()
        if email_subscribe == "":
            self.email_envelope_label.configure(image=self.envelope_cross_image)
        else:
            self.email_envelope_label.configure(image=self.envelope_tick_image)
        
  
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
