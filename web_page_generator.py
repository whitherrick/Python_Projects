import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=1, padx=(10,10), pady=(10,10))

        self.lbl_custom = Label(text="Enter custom text or click Default HTML button")
        self.lbl_custom.grid(row=0, column=0, columnspan=3, padx=(10,10), pady=(10,10))
        self.submitbtn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.submitbtn.grid(row=2, column=2, padx=(10,10), pady=(10,10))
        self.submitentry = Entry(self.master, text="", width= 40)
        self.submitentry.grid(row=1, column=1, columnspan=3, padx=(10,10), pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        customText = self.submitentry.get()
        customFile = open("index.html","w")
        customContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        customFile.write(customContent)
        customFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
