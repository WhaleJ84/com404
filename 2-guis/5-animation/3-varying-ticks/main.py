from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.person_1_image = PhotoImage(file="person_black.gif")
        self.person_2_image = PhotoImage(file="person_red.gif")
        self.person_3_image = PhotoImage(file="person_blue.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.num_ticks = 0
        
        self.person_1_x_pos = 15 
        self.person_1_y_pos = 15
        self.person_1_x_change = 10
        self.person_1_y_change = 0

        self.person_2_x_pos = 425 
        self.person_2_y_pos = 175 
        self.person_2_x_change = -10
        self.person_2_y_change = 0

        self.person_3_x_pos = 15 
        self.person_3_y_pos = 275 
        self.person_3_x_change = 10
        self.person_3_y_change = 0
        
        # add components
        self.add_person_1_image_label()
        self.add_person_2_image_label()
        self.add_person_3_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):

        self.num_ticks += 1
    
        # person 1
        self.person_1_x_pos += self.person_1_x_change
        self.person_1_y_pos += self.person_1_y_change
        self.person_1_image_label.place(x=self.person_1_x_pos,
                                        y=self.person_1_y_pos)
        # hit right
        if self.person_1_x_pos >= 446:
            self.person_1_x_pos = 445
            self.person_1_x_change = 0
            self.person_1_y_change = 10
        # hit bottom
        if self.person_1_y_pos >= 126:
            self.person_1_y_pos = 125
            self.person_1_y_change = 0
            self.person_1_x_change = -10
        # hit left
        if self.person_1_x_pos <= 14:
            self.person_1_x_pos = 15
            self.person_1_x_change = 0
            self.person_1_y_change = -10
        # hit top
        if self.person_1_y_pos <= 14:
            self.person_1_y_pos = 15
            self.person_1_y_change = 0
            self.person_1_x_change = 10
        
        if (self.num_ticks % 4 == 0):
            # person 2
            self.person_2_x_pos += self.person_2_x_change
            self.person_2_y_pos += self.person_2_y_change
            self.person_2_image_label.place(x=self.person_2_x_pos,
                                            y=self.person_2_y_pos)
            
            # hit left
            if self.person_2_x_pos <= 14:
                self.person_2_x_pos = 15
                self.person_2_x_change = 0
                self.person_2_y_change = 10
            # hit bottom
            if self.person_2_y_pos >= 225:
                self.person_2_y_pos = 224
                self.person_2_y_change = 0
                self.person_2_x_change = 10
            # hit right
            if self.person_2_x_pos >= 446:
                self.person_2_x_pos = 445
                self.person_2_x_change = 0
                self.person_2_y_change = -10            
            # hit top
            if self.person_2_y_pos <= 174:
                self.person_2_y_pos = 175
                self.person_2_y_change = 0
                self.person_2_x_change = -10


        if (self.num_ticks % 2 ==0):
            # person 3
            self.person_3_x_pos += self.person_3_x_change
            self.person_3_y_pos += self.person_3_y_change
            self.person_3_image_label.place(x=self.person_3_x_pos,
                                            y=self.person_3_y_pos)
            # hit right
            if self.person_3_x_pos >= 446:
                self.person_3_x_pos = 445
                self.person_3_x_change = 0
                self.person_3_y_change = 10
            # hit bottom
            if self.person_3_y_pos >= 476:
                self.person_3_y_pos = 475
                self.person_3_y_change = 0
                self.person_3_x_change = -10
            # hit left
            if self.person_3_x_pos <= 14:
                self.person_3_x_pos = 15
                self.person_3_x_change = 0
                self.person_3_y_change = -10
            # hit top
            if self.person_3_y_pos <= 274:
                self.person_3_y_pos = 275
                self.person_3_y_change = 0
                self.person_3_x_change = 10
            
        self.after(100, self.tick)

    # the person images
    def add_person_1_image_label(self):
        self.person_1_image_label = Label()
        self.person_1_image_label.place(x=self.person_1_x_pos,
                                        y=self.person_1_y_pos)
        self.person_1_image_label.configure(image=self.person_1_image)

    def add_person_2_image_label(self):
        self.person_2_image_label = Label()
        self.person_2_image_label.place(x=self.person_2_x_pos,
                                        y=self.person_2_y_pos)
        self.person_2_image_label.configure(image=self.person_2_image)

    def add_person_3_image_label(self):
        self.person_3_image_label = Label()
        self.person_3_image_label.place(x=self.person_3_x_pos,
                                        y=self.person_3_y_pos)
        self.person_3_image_label.configure(image=self.person_3_image)
  
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
