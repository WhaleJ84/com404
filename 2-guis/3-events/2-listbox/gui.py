# blueprint for what our gui can do
from tkinter import *
class Gui(Tk):

    # initialise the object
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Song Maker")
        #self.iconbitmap("icon.ico")
        self.configure(bg="#f2eaea",
                       height=300,
                       width=550,
                       bd=15)
    
        #add components/widgets
        self.add_heading_label()
        self.add_lyric_label()
        self.add_lyric_entry()
        self.add_lyric_button()
        self.add_song_label()
        self.add_song_listbox()

    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0,column=0,
                                columnspan=2)
        self.heading_label.configure(text="Song Maker",
                                     font="Arial 24")

    def add_lyric_label(self):
        self.lyric_label = Label()
        self.lyric_label.grid(row=1,column=0,
                              sticky="W")
        self.lyric_label.configure(text="Lyric to add:",
                                   font="Arial 12",
                                   padx=0,
                                   pady=10)

    def add_lyric_entry(self):
        self.lyric_entry = Entry()
        self.lyric_entry.grid(row=2,column=0,
                              sticky="W",
                              columnspan=2)
        self.lyric_entry.configure()

    def add_lyric_button(self):
        self.lyric_button = Button()
        self.lyric_button.grid(row=2,column=1,
                               sticky="E")
        self.lyric_button.configure(text="Add")
        self.lyric_button.bind("<ButtonRelease-1>", self.lyric_button_clicked)

    def add_song_label(self):
        self.song_label = Label()
        self.song_label.grid(row=3,column=0,
                             sticky="W")
        self.song_label.configure(text="Lyrics:",
                                  font="Arial 12",
                                  pady=10)

    def add_song_listbox(self):
        self.song_listbox = Listbox()
        self.song_listbox.grid(row=4,column=0,
                               columnspan=2)
        self.song_listbox.configure(width=30)

    def lyric_button_clicked(self, event):
        lyric_submit = self.lyric_entry.get()
        self.song_listbox.insert(END, lyric_submit)
