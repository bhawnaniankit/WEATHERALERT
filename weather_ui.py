from tkinter import *
import rain

class weather_GUI:
    def __init__(self):
        window=Tk()
        window.title("Weather Alert")
        window.geometry("340x600")
        window.config(bg="black")
        
        canvas=Canvas()
        
        window.mainloop()
        
        
ui=weather_GUI()
