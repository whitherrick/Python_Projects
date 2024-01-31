import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import timedelta
import datetime

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title of GUI window
        self.master.title("File Transfer")
        
        #creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #positions entry in GUI using tkitner grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0,column=1,columnspan=2, padx=(20, 10), pady=(30, 0))

        #creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination",width=20, command=self.destDir)
        #postions destination button in GUI using tkinter grid()
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        #create entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        #creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #postitions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    def sourceDir(self):
        print("hello")
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted into the entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.destination_dir.delete(0,END)
        #The .insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #runs through each file in the source directory
        for i in source_files:
            filePath = os.path.join(source, i)
            fileModTime = os.path.getmtime(filePath)
            twentyFourHours = datetime.datetime.now() - timedelta(hours=24)
            fileDateTime = datetime.datetime.fromtimestamp(fileModTime)
            if twentyFourHours < fileDateTime:
                #moves each file from the source to the destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')

    #creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()


if __name__ =="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
