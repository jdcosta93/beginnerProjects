# Import statements
from tkinter import *
import tkinter as tk
import requests
import datetime as dt

# GUI WITH TKINTER#

# Canvas
root = tk.Tk()
root.geometry("600x500")
root.title("Weather App")
root.resizable(False, False)

# Footer
footer_image = PhotoImage(file="footer.png")
footerimg = Label(root, image=footer_image)
footerimg.place(x=-2, y=350)

# Header
header_image = PhotoImage(file="header.png")
headerimg = Label(root, image=header_image)
headerimg.place(x=30, y=16)

# Text Field for search
textfield = tk.Entry(root, justify= "center", width= 17, font=("poppins", 25, "bold"), bd=0, highlightthickness=0, fg="black",bg="white")
textfield.place(x=50, y=40)
textfield.focus()

# Bottom Labels 

Label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"),bg="#4A8CC2")
Label1.place(x= 50, y= 400)
Label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"),bg="#4A8CC2")
Label2.place(x= 150, y= 400)
Label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"),bg="#4A8CC2")
Label3.place(x= 270, y= 400)
Label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"),bg="#4A8CC2")
Label4.place(x= 460, y= 400)
w = Label(text = "-", font=("arial", 20, "bold"),bg="#4A8CC2")
w.place(x=40, y=430)
h = Label(text = "-", font=("arial", 20, "bold"),bg="#4A8CC2")
h.place(x=165, y=430)
d = Label(text = "-", font=("arial", 20, "bold"),bg="#4A8CC2")
d.place(x=255, y=430)
p = Label(text = "-", font=("arial", 20, "bold"),bg="#4A8CC2")
p.place(x=475, y=430)

# Time/Weather/Temperature Labels 

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

wtr = Label(font=("arial", 40, "bold"))
wtr.place(x=410, y=250)

# Weather images

wtr_rain = PhotoImage(file="rain.png")
wtrrain = Label(root, image=wtr_rain)  
wtrrain.place(x= -111200, y= -111100)

sun_image = PhotoImage(file="sun.png")
sun = Label(root, image=sun_image)
sun.place(x= -111200, y= -111100)

snow_image = PhotoImage(file="snow.png")
snow = Label(root, image= snow_image)
snow.place(x= -111200, y= -111100)

cloud_image = PhotoImage(file="cloud.png")
cloud = Label(root, image= cloud_image)
cloud.place(x= -111200, y= -111100)

fog_image = PhotoImage(file="fog.png")
fog = Label(root, image= fog_image)
fog.place(x= -111200, y= -111100)

name = Label(font=("arial", 25, "bold"), fg="white")
name.place(x=400, y=80)

# FUNCTION TO FETCH WEATHER CONDITIONS WITH OPENWEATHERMAP API #
def getWeather(root):
    
    destination = textfield.get()
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="
    API_KEY = "534971e00969ed72a39101014a720d7e"
    URL = BASE_URL + destination + "&appid=" + API_KEY 

    response = requests.get(URL).json()
    
    temp = str(int(response['main']['temp'] - 273.15)) + " °C"
    wind = str(response['wind']['speed']) + " m/s"
    pressure = str(response['main']['pressure']) + " hPa"
    humidity = str(response['main']['humidity']) + " %"
    weather = str(response['weather'][0]['main'])
    description = response['weather'][0]['description'].title()
    
    # Conditional statements to show images based on weather condition
    
    if "Rain" in weather:
        wtrrain.place(x= 50, y= 100)
    else:
        wtrrain.place(x= -111200, y= -111100)
        
    if "lear" in weather:
        sun.place(x= 35, y= 90)
    else:
        sun.place(x= -111200, y= -111100)
        
    if "now" in weather:
        snow.place(x= 100, y= 80)
    else:
        snow.place(x= -111200, y= -111100)
        
    if "loud" in weather or "cast" in weather:
        cloud.place(x= 100, y= 100)
    else:
        cloud.place(x= -111200, y= -111100) 
        
    if "og" in weather or "aze" in weather or "ist" in weather:
        fog.place(x= 100, y= 100)
    else:
        fog.place(x= -111200, y= -111100) 
        
    # Config to display the data received from get request into bottom labels
    
    t.config(text=temp, fg="#ee666d")
    w.config(text=wind, fg="black")
    h.config(text=humidity, fg="black")
    d.config(text=description, fg="black")
    p.config(text=pressure, fg="black")
    name.config(text="CURRENT \n WEATHER")
    wtr.config(text=weather, fg="white")

textfield.bind('<Return>', getWeather)
root.mainloop()