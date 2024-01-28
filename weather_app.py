from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests


def get_wether_info():
    city = city_name.get()
    api_key = "cccc4c61c68c7fc23e9e2ac3fd535510"
    
    try:
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()

        # Check if the "weather" key is present in the response
        if "weather" in data:
            w_label1.config(text=data["weather"][0]["main"])
            wb_label1.config(text=data["weather"][0]["description"])
            temp_label1.config(text=f"{data['main']['temp'] - 273.15:.2f}°C")
            pre_label1.config(text=data["main"]["pressure"])
        else:
            # Handle the case where the "weather" key is not present
            w_label1.config(text="N/A")
            wb_label1.config(text="N/A")
            temp_label1.config(text="N/A")
            pre_label1.config(text="N/A")

    except Exception as e:
        # Handle other exceptions (e.g., network issues, invalid JSON)
        print(f"An error occurred: {e}")
        w_label1.config(text="Error")
        wb_label1.config(text="Error")
        temp_label1.config(text="Error")
        pre_label1.config(text="Error")

    
    
    
window = tk.Tk()    
window.title("Weather application")
window.config(bg= "#87CEEB")
window.geometry("500x500")


name_label = Label(window,text="Weather application", font= ("Time New Roman", 20, "bold"))
name_label.place(x=20,y=20,height=35,width=470)

countries = cities = [
    "Amsterdam",
    "Bangkok",
    "Beijing",
    "Berlin",
    "Buenos Aires",
    "Cairo",
    "Cape Town",
    "Chicago",
    "Delhi",
    "Dubai",
    "Dublin",
    "Istanbul",
    "Jakarta",
    "Kathmandu",
    "Lagos",
    "Lima",
    "Lisbon",
    "London",
    "Los Angeles",
    "Madrid",
    "Marrakech",
    "Mexico City",
    "Moscow",
    "Mumbai",
    "Nairobi",
    "New York City",
    "Oslo",
    "Paris",
    "Prague",
    "Rio de Janeiro",
    "Rome",
    "San Francisco",
    "Seoul",
    "Shanghai",
    "Singapore",
    "Stockholm",
    "Sydney",
    "Tokyo",
    "Toronto",
    "Vancouver",
    "Vienna",
    "Warsaw",
    "Zurich",
    "Barcelona",
    "Bogotá",
    "Havana",
    "Helsinki",
    "Hong Kong",
]


city_name = StringVar()
com = ttk.Combobox(window,text="Weather",values=countries ,font= ("Time New Roman", 10),textvariable= city_name)
com.place(x=100,y=70,height=30,width=300)


w_label = Label(window,text="Weather Climate", font= ("Time New Roman", 10, "bold"))
w_label.place(x=80,y=250,height=20,width=150)
w_label1 = Label(window,text="", font= ("Time New Roman", 10, "bold"))
w_label1.place(x=250,y=250,height=20,width=150)


wb_label = Label(window,text="Weather discription", font= ("Time New Roman", 10, "bold"))
wb_label.place(x=80,y=280,height=20,width=150)
wb_label1 = Label(window,text="", font= ("Time New Roman", 10, "bold"))
wb_label1.place(x=250,y=280,height=20,width=150)


temp_label = Label(window,text="Temperature", font= ("Time New Roman", 10, "bold"))
temp_label.place(x=80,y=310,height=20,width=150)
temp_label1 = Label(window,text="", font= ("Time New Roman", 10, "bold"))
temp_label1.place(x=250,y=310,height=20,width=150)


pre_label = Label(window,text="Pressure", font= ("Time New Roman", 10, "bold"))
pre_label.place(x=80,y=340,height=20,width=150)

pre_label1 = Label(window,text="", font= ("Time New Roman", 10, "bold"))
pre_label1.place(x=250,y=340,height=20,width=150)



button = Button(window, text="Show", font= ("Time New Roman", 10),command= get_wether_info)
button.place(x = 230 , y= 110 , height= 30, width= 50)

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y -35}")

window.mainloop()