import mail
import  rain
from tkinter import *
from tkinter import messagebox
import datetime

degree_sign = u'\N{DEGREE SIGN}'
CITY="Chennai"

def temp(weather_data):
    return round(weather_data[1]["main"]["temp"]-273)
    
window=Tk()
window.title("Weather Alert")
window.geometry("340x600")
now=datetime.datetime.now()
window.config(bg="black")
canvas=Canvas(bg="black")
canvas.config(highlightthickness=0,width=340,height=600)

weather=rain.weathe_city(CITY)
id=weather[1]["weather"][0]["id"]
id=302
background=None
text_color="white"

if 499<id<532 or 299<id<322 or 199<id<233:
    background=PhotoImage(file="./img/rain.png")
    text_color="white"
    
elif(id==800):
    background=PhotoImage(file="./img/sunny.png")
    text_color="black"
    
elif 800<id<805:
    background=PhotoImage(file="./img/clouds.png")
    text_color="white"
    

canvas.create_image(170,300,image=background)
city=canvas.create_text(170,75,text=CITY,fill=text_color,font=('Helvetica',12,"normal" ))
temperature=canvas.create_text(170,110,text=f"{temp(weather)}{degree_sign}",fill=text_color,font=('Helvetica',35,"bold" ))

canvas.create_line(0, 340, 340, 340, width=1,fill=text_color)
canvas.pack()


canvas.pack(side='top', fill='both', expand='yes')



if weather[0]:
    mail.alert_email("bhawnaniankit@gmail.com")
    messagebox.showwarning("Weather Alert","")
    
window.mainloop()
