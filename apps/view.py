import tkinter
from tkinter import *

class View(object): 

    def __init__(self, master): 
        self.master = master

    def main_view(self): 
        top = tkinter.Tk() 
        top.mainloop()
    
if __name__ == "__main__": 
    a = View()
    a.main_view()

