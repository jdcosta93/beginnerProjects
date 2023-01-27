# Import statements
from tkinter import *
import tkinter as tk
import requests
from datetime import datetime as dt
import pytz
from pytz import timezone
from geopy.geocoders import Nominatim as Nm
from timezonefinder import TimezoneFinder

# GUI WITH TKINTER#
# Canvas
root = tk.Tk()
root.geometry("600x500")
root.title("Weather App")
root.resizable(False, False)

# Footer
footer_image = PhotoImage(file="images/footer.png")
footerimg = Label(root, image=footer_image)
footerimg.place(x=-2, y=350)

# Header
header_image = PhotoImage(file="images/header.png")
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
Label4.place(x= 475, y= 400)
w = Label(text = "-", font=("arial", 20, "bold"),bg="#4A8CC2")
w.place(x=40, y=430)
h = Label(text = "-", font=("arial", 20, "bold"),bg="#4A8CC2")
h.place(x=165, y=430)
d = Label(text = "-", font=("arial", 20, "bold"),bg="#4A8CC2")
d.place(x=270, y=430)
p = Label(text = "-", font=("arial", 20, "bold"),bg="#4A8CC2")
p.place(x=475, y=430)

# Time/Weather/Temperature Labels 
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

wtr = Label(font=("arial", 40, "bold"))
wtr.place(x=410, y=250)

tm = Label(font=("arial", 30, "bold"), fg="black")
tm.place(x=400 ,y=320)
# Weather images

wtr_rain = PhotoImage(file="images/rain.png")
wtrrain = Label(root, image=wtr_rain)  
wtrrain.place(x= -111200, y= -111100)

clear_image = PhotoImage(file="images/clear.png")
clear = Label(root, image=clear_image)
clear.place(x= -111200, y= -111100)

snow_image = PhotoImage(file="images/snow.png")
snow = Label(root, image= snow_image)
snow.place(x= -111200, y= -111100)

cloud_image = PhotoImage(file="images/cloud.png")
cloud = Label(root, image= cloud_image)
cloud.place(x= -111200, y= -111100)

fog_image = PhotoImage(file="images/fog.png")
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
    
    # Getting correct time zone and displaying current time 
    tf = TimezoneFinder()
    geolocator = Nm(user_agent="geoapiExercises")
    location = geolocator.geocode(destination)
    coords = tf.timezone_at(lng=location.longitude,lat=location.latitude)
    time_zone = pytz.timezone(coords)
    local_time_now = dt.now(time_zone)
    local_time = local_time_now.strftime("%H:%M %Z")

    # Conditional statements to show images based on weather condition
    if "ain" in weather or "izzle" in weather:
        wtrrain.place(x= 50, y= 100)
    else:
        wtrrain.place(x= -111200, y= -111100)
        
    if "lear" in weather or "sun" in weather:
        clear.place(x= 0, y= 90)
    else:
        clear.place(x= -111200, y= -111100)
        
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
    tm.config(text=local_time, fg="#ee666d")
    t.config(text=temp, fg="#ee666d")
    w.config(text=wind, fg="black")
    h.config(text=humidity, fg="black")
    d.config(text=description, fg="black")
    p.config(text=pressure, fg="black")
    name.config(text="CURRENT \n WEATHER")
    wtr.config(text=weather, fg="white")
    
textfield.bind('<Return>', getWeather)
root.mainloop()