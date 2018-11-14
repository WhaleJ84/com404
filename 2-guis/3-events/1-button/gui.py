# blueprint for what our gui can do
from tkinter import *
class Gui(Tk):

    # initialise the object
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Newsletter")
        self.iconbitmap("icon.ico")
        self.configure(bg="#f2eaea",
                       borderwidth=15,
                       height=300,
                       width=550)
    
        #add components/widgets
        self.add_program_frame()
        self.add_heading_label()
        self.add_message_label()
        self.add_email_frame()
        self.add_email_label()
        self.add_email_entry()
        self.add_email_image()
        self.add_submit_button()

    def add_program_frame(self):
        self.program_frame = Frame()
        self.program_frame.pack(fill=BOTH)
        self.program_frame.configure(bg="#f9f9f9")

    def add_heading_label(self):
        # 1. create the component object
        self.heading_label = Label(self.program_frame)
        self.heading_label.pack(fill=X,
                                side=TOP)
        # 2. style the component
        self.heading_label.configure(font="Arial 24",
                                     bg="#f9f9f9",
                                     padx=10,
                                     pady=10,
                                     text="RECEIVE OUR NEWSLETTER")

    def add_message_label(self):
        self.message_label = Label(self.program_frame)
        self.message_label.pack(side=TOP)
        self.message_label.configure(font="Arial 12",
                                     bg="#f9f9f9",
                                     pady=10,
                                     text="Please enter your email below to receive our newsletter.")

    def add_email_frame(self):
        self.email_frame = Frame(self.program_frame)
        self.email_frame.pack()
        self.email_frame.configure(pady=20,
                                   bg="#f9f7f7")

    def add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        self.email_label.configure(font="Arial 12",
                                   bg="#f9f9f9",
                                   text="Email:")

    def add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=LEFT)
        self.email_entry.configure(width=45,
                                   bg="#f9f9f9")

    def add_email_image(self):
        #picture = PhotoImage(file="picture.png")
        #self.email_image = Label(self.email_frame)
        #self.email_image.pack(side=RIGHT)
        #self.email_image.configure(image=picture)
        pass

    def add_submit_button(self):
        self.submit_button = Button(self.program_frame)
        self.submit_button.pack(side=BOTTOM, fill=X)
        self.submit_button.configure(font="Arial 12",
                                      text="Subscribe",
                                      bg="#f2eaea",
                                      relief=RAISED)
        # bind events
        self.submit_button.bind("<ButtonRelease-1>", self.submit_button_clicked)

    def submit_button_clicked(self, event):
        email_subscribe = self.email_entry.get()
        messagebox.showinfo("Gui", "Your email " + email_subscribe + " has been added.")
