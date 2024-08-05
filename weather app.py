from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk


app=Tk()
app.title("Weather App")
app.geometry("900x500+300+200")
app.resizable(False,False)

def get_weather():
    city=textzone.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    cc=TimezoneFinder()
    result=cc.timezone_at(lng=location.longitude,lat=location.latitude)
    
    pyt=pytz.timezone(result)
    local_time=datetime.now(pyt)
    time=local_time.strftime("%H: %M %p")
    clock.config(text=time)
    name.config(text="CURRENT WEATHER",fg="LightBlue")

    api_key="be97b9f4bcdf753f087803fdbb2ccf3b"
    lat = location.latitude
    lon = location.longitude
    #weather
    api=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    json_data=requests.get(api).json()

    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']

    t.config(text=(temp,"°C"))
    c.config(text=(condition,"|","FEELS", "LIKE",temp,"°C"))
    q.config(text=wind)
    w.config(text=humidity)
    e.config(text=description)
    r.config(text=pressure)

#search box 
barre_image=PhotoImage(file="barre.png.png")
my_image=Label(image=barre_image)
my_image.place(x=20,y=20)

textzone=tk.Entry(app,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textzone.place(x=50,y=40)
textzone.focus()

search_logo=PhotoImage(file="search_logo.png")
my_image_logo=Button(image=search_logo,borderwidth=0,cursor="hand2",bg="#404040",command=get_weather)
my_image_logo.place(x=400,y=34)

#logo

logo_im=PhotoImage(file="loogo-removebg-preview (2).png")
logo=Label(image=logo_im)
logo.place(x=105,y=120)

# loogo1 
logo1=PhotoImage(file="Picsart_24-07-18_21-25-43-400 (4).png")
loogo=Label(image=logo1)
loogo.place(x=550,y=40)

logo11=PhotoImage(file="Picsart_24-07-18_21-26-03-207.png")
looogo=Label(image=logo11)
looogo.place(x=670,y=40)

logo12=PhotoImage(file="Picsart_24-07-18_21-26-21-268.png")
loooogo=Label(image=logo12)
loooogo.place(x=790,y=40)




#bottom box
frame_image=PhotoImage(file="Copy of box.png")
frame_myimage=Label(image=frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#define time
name=Label(app,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(app,font=("Helvetica",20))
clock.place(x=30,y=130)
#label
label1=Label(app,text="Wind",font=("Helvetica",15,'bold'),fg="yellow",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(app,text="Humidity",font=("Helvetica",15,'bold'),fg="yellow",bg="#1ab5ef")
label2.place(x=268,y=400)

label3=Label(app,text="Description",font=("Helvetica",15,'bold'),fg="yellow",bg="#1ab5ef")
label3.place(x=470,y=400)

label4=Label(app,text="Pressure",font=("Helvetica",15,'bold'),fg="yellow",bg="#1ab5ef")
label4.place(x=690,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"),fg="#ee666d")
c.place(x=400,y=250)

q=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef",fg="White")
q.place(x=123,y=430)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef",fg="White")
w.place(x=274,y=430)

e=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef",fg="White")
e.place(x=475,y=430)

r=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef",fg="White")
r.place(x=695,y=430)

app.mainloop()
