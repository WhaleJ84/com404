from tkinter import *
from tkinter import messagebox
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.envelope_image = PhotoImage(file="envelope.gif")
        self.envelope_tick_image = PhotoImage(file="envelope_tick.gif")
        self.envelope_cross_image = PhotoImage(file="envelope_cross.gif")
        self.weekly_newsletter_image = PhotoImage(file="weekly_newsletter.gif")
        self.monthly_newsletter_image = PhotoImage(file="monthly_newsletter.gif")
        self.yearly_newsletter_image = PhotoImage(file="yearly_newsletter.gif")
        
        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#eee",
                       padx=10, pady=10)

        # set animation attributes
        self.newsletter_x_pos = 50
        self.newsletter_y_pos = 50
        self.newsletter_x_change = 0
        self.newsletter_y_change = 0
        
        # add components
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
        self.add_animation_button()
        self.add_animation_frame()
        self.add_animation_label()

        # animation state
        self.animation_state = int(2)
        
        # start the timer
        self.tick()

    # timer
    def tick(self):
        self.newsletter_x_pos += self.newsletter_x_change
        self.newsletter_y_pos += self.newsletter_y_change
        self.animation_label.place(x=self.newsletter_x_pos,
                                   y=self.newsletter_y_pos)
        if self.newsletter_x_pos >= 210:
            self.newsletter_x_change *= -1
        if self.newsletter_y_pos >= 141:
            self.newsletter_y_change *= -1
        if self.newsletter_x_pos <= 5:
            self.newsletter_x_change *= -1
        if self.newsletter_y_pos <= 5:
            self.newsletter_y_change *= -1

        self.after(100,self.tick)

    # heading
    def add_heading_label(self):
        self.window_frame = Label()
        self.window_frame.pack(fill=X,
                               side=TOP)
        self.window_frame.configure(text="RECEIVE OUR NEWSLETTER",
                                    font="Arial 14",
                                    pady=10)

    # instruction
    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.pack(fill=X,
                                    side=TOP)
        self.instruction_label.configure(text="Please enter your email below to receive our newsletter.",
                                         padx=10, pady=10)

    # email
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
        
    # interval
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
        self.periodic_optionmenu.bind("<KeyRelease>", self.animation_button_clicked)
        

    # subscribe
    def add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.pack(fill=X)
        self.subscribe_button.configure(text="Subscribe",
                                        bg="#fee")
        self.subscribe_button.bind("<ButtonRelease-1>", self.subscribe_button_clicked)

    # animation
    def add_animation_button(self):
        self.animation_button = Button()
        self.animation_button.pack(fill=X)
        self.animation_button.configure(text="Start Animation",
                                        bg="#fee")
        self.animation_button.bind("<ButtonRelease-1>", self.animation_button_clicked)

    def add_animation_frame(self):
        self.animation_frame = Frame()
        self.animation_frame.pack(fill=X)
        self.animation_frame.configure(bg="#fed",
                                       height=200)

    def add_animation_label(self):
        self.animation_label = Label(self.animation_frame)
        self.animation_label.place(x=self.newsletter_x_pos,
                                   y=self.newsletter_y_pos)
        self.animation_label.configure(image="")

    # functions
    def subscribe_button_clicked(self, event):
        self.periodic_choice = self.variable.get()
        email_subscribe = self.email_entry.get()
        if email_subscribe == "":
            messagebox.showinfo("Newsletter", "Please enter your email!")
        elif email_subscribe != "" and self.periodic_choice == "Weekly":
            messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter! You will receive this every Monday.")
        elif email_subscribe != "" and self.periodic_choice == "Monthly":
            messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter! You will receive this on the first day of each month.")
        elif email_subscribe != "" and self.periodic_choice == "Yearly":
            messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter! You will receive this at the start of each year.")
        else:
            messagebox.showinfo(":(", "Error.")

    def email_entry_edit(self, event):
        email_subscribe = self.email_entry.get()
        if email_subscribe == "":
            self.email_envelope_label.configure(image=self.envelope_cross_image)
        else:
            self.email_envelope_label.configure(image=self.envelope_tick_image)

    def animation_button_clicked(self, event):
        self.periodic_choice = self.variable.get()
        self.animation_state += 1
        print(self.animation_state)
        # animation stop
        if self.animation_state % 2 == 0:
            self.animation_button.configure(text="Start Animation")
            self.newsletter_x_change = 0
            self.newsletter_y_change = 0
        # animation start
        elif self.animation_state % 2 == 1:
            self.animation_button.configure(text="Stop Animation")
            if self.periodic_choice == "Weekly":
                self.animation_label.configure(image=self.weekly_newsletter_image)
                self.newsletter_x_change = 10
                self.newsletter_y_change = 10               
            elif self.periodic_choice == "Monthly":
                self.animation_label.configure(image=self.monthly_newsletter_image)
                self.newsletter_x_change = 10
                self.newsletter_y_change = 10
            elif self.periodic_choice == "Yearly":
                self.animation_label.configure(image=self.yearly_newsletter_image)
                self.newsletter_x_change = 10
                self.newsletter_y_change = 10
            else:
                print("Error.") 
  
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
