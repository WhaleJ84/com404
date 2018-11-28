from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="ball.gif")
        self.ball_2_image = PhotoImage(file="blue_ball.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.ball_x_pos = 250
        self.ball_y_pos = 30
        self.ball_x_change = 10
        self.ball_y_change = 10

        self.ball_2_x_pos = 30
        self.ball_2_y_pos = 250
        self.ball_2_x_change = 10
        self.ball_2_y_change = 10
        
        # add components
        self.add_ball_image_label()
        self.add_ball_2_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        if self.ball_x_pos >= 475:
            self.ball_x_change *= -1
        if self.ball_y_pos >= 475:
            self.ball_y_change *= -1
        if self.ball_x_pos <= 5:
            self.ball_x_change *= -1
        if self.ball_y_pos <= 5:
            self.ball_y_change *= -1
            
        self.ball_2_x_pos = self.ball_2_x_pos + self.ball_2_x_change
        self.ball_2_y_pos = self.ball_2_y_pos + self.ball_2_y_change
        self.ball_2_image_label.place(x=self.ball_2_x_pos,
                                      y=self.ball_2_y_pos)
        if self.ball_2_x_pos >= 475:
            self.ball_2_x_change *= -1
        if self.ball_2_y_pos >= 475:
            self.ball_2_y_change *= -1
        if self.ball_2_x_pos <= 5:
            self.ball_2_x_change *= -1
        if self.ball_2_y_pos <= 5:
            self.ball_2_y_change *= -1
        self.after(100, self.tick)

    # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)

    def add_ball_2_image_label(self):
        self.ball_2_image_label = Label()
        self.ball_2_image_label.place(x=self.ball_2_x_pos,
                                      y=self.ball_2_y_pos)
        self.ball_2_image_label.configure(image=self.ball_2_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
