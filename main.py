from tkinter import *
import tkinter as tk
from geopy.geocoders import Photon
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root = Tk()
root.title("Weather App")
# "900X500" = How big the window is and "300+200" = Centering the window on screen
root.geometry("900x500+300+200")
root.resizable(False,False)
# root.wm_attributes('-transparent',0.5)

def getWeather():

    try:

        # Returns a location for the zone
        city = textfield.get()
        geolocator = Photon(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        # From location, gets time
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        # The string is to format time
        # It goes "Hour:Minutes AM OR PM"
        current_time = local_time.strftime("%I:%M %p")
        # Edit text to update time
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # actual weather part
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid=90e9159a67b02b06baa3c5feb2191d97"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        temp = (temp * 9/5) +32
        feels_like = int(json_data['main']['feels_like']-273.15)
        feels_like = (feels_like * 9/5) +32
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text =(temp,"°"))
        c.config(text =(condition,"|", "FEELS", "LIKE", feels_like, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!")


# search box
# Open photo
Search_image = PhotoImage(file="search.png")
# Makes the photo a widget which has lots of attributes like place
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

# allows user to type in the search bar photo
#BUG HERE - can't seem to make the textfield take the same shape and size as the serach image
textfield = tk.Entry(root, justify="center", width=17,font=("poppins", 25, "bold"), bg="#181818", borderwidth=0, border=0, highlightthickness=0 )
textfield.place(x=50, y=40)
textfield.focus()

# makes a button for searching
#BUG - Same as before, bg color no good
Search_icon = PhotoImage(file="new_search.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#181818", command=getWeather)
myimage_icon.place(x=400,y=34)

# place logo
logo_image=PhotoImage(file="logo.png")
myimage_logo = Label(image=logo_image)
myimage_logo.place(x=150,y=100)

# Bottom box image
Frame_image = PhotoImage(file="box.png")
myimage_frame = Label(image=Frame_image)
myimage_frame.pack(padx=5,pady=5,side=BOTTOM)

# time
name = Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock = Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

# label for wind
label_1 = Label(root,text="WIND",font=("Helvetic",15,'bold'),fg="white",bg="#1E9ED9")
label_1.place(x=120,y=400)

# label for humidity
label_2 = Label(root,text="HUMIDITY",font=("Helvetic",15,'bold'),fg="white",bg="#1E9ED9")
label_2.place(x=250,y=400)

# label for description
label_3 = Label(root,text="DESCRIPTION",font=("Helvetic",15,'bold'),fg="white",bg="#1E9ED9")
label_3.place(x=430,y=400)

# label for pressure
label_4 = Label(root,text="PRESSURE",font=("Helvetic",15,'bold'),fg="white",bg="#1E9ED9")
label_4.place(x=650,y=400)

# labels for bottom box
t=Label(font=("arial",70,'bold'),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)
w=Label(text="...",font=("arial",20,"bold"),fg = "black",bg="#1E9ED9")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),fg = "black",bg="#1E9ED9")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),fg = "black",bg="#1E9ED9")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),fg = "black",bg="#1E9ED9")
p.place(x=670,y=430)

# Allows program to run constantly
root.mainloop()

