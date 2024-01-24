# Python ver: 3.11.7
#
# Author: Whitney Herrick
#
# Purpose: Phonebook Project. Learning OOP, Tkinter GUI module,
#           using Tkinter parent and child relationships.


from tkinter import *
import tkinter as tk
from tkinter import messagebox

#importing our other modules so we have access to them
import phonebook_gui
import phonebook_func

#Frame is the Tkinter frame class our class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #Define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width in pixels)
        self.master.maxsize(500,300)
        #This centerwindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        #This protocol method is a tkinter built-in method to catch if
        #the user clicks the upper corner, "x" on windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets from a separate module,
        #keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
