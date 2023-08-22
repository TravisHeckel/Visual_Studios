import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        #This creates the label instructing the user on what to do.
        self.lbl_instruct = tk.Label(self.master, text = 'Enter custom text or click the Default HTML page Button ')
        self.lbl_instruct.grid(row = 0, column = 0, padx = (10,10), pady = (10, 10), sticky = N+W)
        #This reflects the input area for the user to put a custom message
        self.txt_input = tk.Entry(self.master, text = '', width = 130)
        self.txt_input.grid(row = 1, column = 0, columnspan = 4,  padx=(25,25), pady=(10,10), sticky =N + W)
        #This is the first button to put make a default html page
        self.btn = Button(self.master, text="Default HTML Page", width = 30, height = 2, command=self.defaultHTML)
        self.btn.grid(row = 2, column = 2, padx=(10,10), pady=(10,10))
        #this is hte secon button to put make a custom message page
        self.btn = Button(self.master, text="Submit Custom Text", width = 30, height = 2, command=self.customtext)
        self.btn.grid(row = 2, column = 3, padx=(10,10), pady=(10,10))
        

        
    #This function activates when the button is hit, this will create a HTML page with a default message
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer Sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    #This function activates when the button is hit, this will create a HTML page with the line of custom text
    def customtext(self):
        customerword= self.txt_input.get()
        htmlText = customerword
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
