from tkinter import *
from tkinter import messagebox
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.tick_image = PhotoImage(file="circle_tick.gif")
        self.cross_image = PhotoImage(file="circle_cross.gif")
        self.person_image = PhotoImage(file="person.gif")
        self.person_gbp_image = PhotoImage(file="person_£.gif")
        self.person_euro_image = PhotoImage(file="person_€.gif")
        self.person_usd_image = PhotoImage(file="person_$.gif")
        self.house_image = PhotoImage(file="house.gif")
        
        # window attributes
        self.title("Currency Converter")
        self.configure(bg="#ffe8e8",
                       padx=10, pady=10)

        # animation attributes
        self.person_x_pos = 25
        self.person_y_pos = 80
        self.person_x_change = 0
        self.person_y_change = 0

        # add components
        self.add_header_label()
        self.add_amount_frame()
        self.add_amount_label()
        self.add_amount_entry()
        self.add_amount_image()
        self.add_currency_frame()
        self.add_from_label()
        self.add_from_optionmenu()
        self.add_to_label()
        self.add_to_optionmenu()
        self.add_button_frame()
        self.add_clear_button()
        self.add_convert_button()
        self.add_currency_message()
        self.add_simulate_button()
        self.add_animation_frame()
        self.add_anim1_label()
        self.add_anim2_label()

        # timer
        self.tick()

    # tick
    def tick(self):
        self.person_x_pos += self.person_x_change
        self.person_y_pos += self.person_y_change
        self.anim1_label.place(x=self.person_x_pos,
                               y=self.person_y_pos)
        if self.person_x_pos >=200:
            self.person_x_change = 0
        self.after(100,self.tick)
     
    # header
    def add_header_label(self):
        self.header_label = Label()
        self.header_label.pack(side=TOP)
        self.header_label.configure(text="Currency Converter",
                                    font="Arial 24",
                                    bg="#ffe8e8")

    # amount
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
        self.amount_entry.bind("<KeyRelease>",self.amount_entered)

    def add_amount_image(self):
        self.amount_image = Label(self.amount_frame)
        self.amount_image.grid(row=1,column=3,
                               sticky=E)
        self.amount_image.configure(image="")

    # currency exchange
    def add_currency_frame(self):
        self.currency_frame = Frame()
        self.currency_frame.pack(side=TOP,
                                 fill=X)
        self.currency_frame.configure(bg="#ffe8e8")
        
    def add_from_label(self):
        self.to_label = Label(self.currency_frame)
        self.to_label.grid(row=0,column=0,
                           sticky=W)
        self.to_label.configure(text="From",
                                bg="#ffe8e8")
        
    def add_from_optionmenu(self):
        self.from_currency = StringVar()
        self.FROM_OPTIONS = ("GBP","Euros")
        self.from_currency.set("GBP")
        self.from_optionmenu = OptionMenu(self.currency_frame,self.from_currency, *self.FROM_OPTIONS)
        self.from_optionmenu.grid(row=1,column=0,
                                  columnspan=3)
        self.from_optionmenu.configure(width=44)

    def add_to_label(self):
        self.to_label = Label(self.currency_frame)
        self.to_label.grid(row=2,column=0,
                           sticky=W)
        self.to_label.configure(text="To",
                                bg="#ffe8e8")

    def add_to_optionmenu(self):
        self.to_currency = StringVar()
        self.TO_OPTIONS = ("Euros","USD")
        self.to_currency.set("Euros")
        self.to_optionmenu = OptionMenu(self.currency_frame,self.to_currency, *self.TO_OPTIONS)
        self.to_optionmenu.grid(row=3,column=0,
                                columnspan=3)
        self.to_optionmenu.configure(width=44)

    # buttons
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
        self.clear_button.bind("<ButtonRelease-1>", self.clear_clicked)

    def add_convert_button(self):
        self.convert_button = Button(self.button_frame)
        self.convert_button.pack(side=RIGHT)
        self.convert_button.configure(text="Convert",
                                      width=10)
        self.convert_button.bind("<ButtonRelease-1>", self.convert_clicked)

    # display
    def add_currency_message(self):
        self.text = StringVar()
        self.text.set("System Message Displayed Here")
        self.currency_message = Message(textvariable=self.text)
        self.currency_message.pack(fill=X)
        self.currency_message.configure(bg="#fffbce",
                                        aspect=1000,
                                        relief=SUNKEN)
    # animation
    def add_simulate_button(self):
        self.simulate_button = Button()
        self.simulate_button.pack(side=TOP,
                                  pady=10)
        self.simulate_button.configure(text="Simulate")
        self.simulate_button.bind("<ButtonRelease-1>",self.simulate_clicked)

    def add_animation_frame(self):
        self.animation_frame = Frame()
        self.animation_frame.pack(side=TOP,
                                  fill=X)
        self.animation_frame.configure(bg="#ded",
                                       height=200)

    def add_anim1_label(self):
        self.anim1_label = Label(self.animation_frame)
        self.anim1_label.place(x=self.person_x_pos,
                               y=self.person_y_pos)
        self.anim1_label.configure(image=self.person_image)

    def add_anim2_label(self):
        self.anim2_label = Label(self.animation_frame)
        self.anim2_label.place(x=200,y=35)
        self.anim2_label.configure(image=self.house_image)

    
    # events
    def amount_entered(self,event):
        self.entry_value = int(self.amount_entry.get())
        if self.entry_value == "":
            self.amount_image.configure(image=self.cross_image)
        else:
            self.amount_image.configure(image=self.tick_image)

    def convert_clicked(self,event):
        GBP_Euro = 1.15
        GBP_USD = 1.42
        Euro_USD = 1.24
        self.conversion_rate = 1
        if self.from_currency.get() == "GBP" and self.to_currency.get() == "Euros":
            self.conversion_rate = GBP_Euro
        elif self.from_currency.get() == "GBP" and self.to_currency.get() == "USD":
            self.conversion_rate = GBP_USD
        elif self.from_currency.get() == "Euros" and self.to_currency.get() == "USD":
            self.conversion_rate = Euro_USD
        self.conversion_total = int(self.entry_value * self.conversion_rate)
        self.text.set("Converting...")
        messagebox.showinfo("Conversion", "{} from {} to {} with a rate of {} is {}".format(self.entry_value,self.from_currency.get(),self.to_currency.get(),self.conversion_rate,self.conversion_total))

    def clear_clicked(self,event):
        self.text.set("System Message Displayed Here")
        self.amount_entry.delete(0,END)

    def simulate_clicked(self,event):
        self.person_x_pos = 25
        self.person_y_pos = 80
        if self.from_currency.get() == "GBP":
            self.anim1_label.configure(image=self.person_gbp_image)
            self.person_x_change = 10
        elif self.from_currency.get() == "Euros":
            self.anim1_label.configure(image=self.person_euro_image)
            self.person_x_change = 10
  
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
