from re import I
import tkinter as tk
from tkinter import Variable, filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

my_w = customtkinter.CTk()
my_w.geometry("980x720")
my_w.config(padx=340, pady=20)  # Size of the window 
my_w.title('www.plus2net.com')
my_font1=('times', 18, 'bold')
l1 = customtkinter.CTkLabel(text="Add a photo.") 
l1.grid(row=1,column=1)
b1 = customtkinter.CTkButton(my_w, text='Upload File', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=0)
b1 = customtkinter.CTkButton(my_w, text='Change Logo', 
   width=20,command = lambda:upload_logo())
b1.grid(row=2,column=2)
b1.config(pady=10, padx=20)









def upload_file():
    global filename1
    global e1
    global s1
    global s2
    global logo_path
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 

    filename1 = filedialog.askopenfilename(filetypes=f_types)
    
    img=Image.open(filename1).convert("RGBA")
    
    logo_path = "true.png"
    logo=Image.open(logo_path).convert("RGBA") 
    img=img.resize((300,300))

    img.paste(logo, (240, 240))
 
    img=ImageTk.PhotoImage(img)
    e1 =tk.Label(my_w)
    e1.grid(row=3,column=1)
    e1.image = img
    
        
    e1['image']=img  
        
    s1 = customtkinter.CTkSlider(my_w, orient="vertical", from_= 5, to=100, command= slide_ver)
    s1.grid(row=3, column=3)
    ll = customtkinter.CTkLabel(my_w, text=" ")
    ll.grid(row=4, column=1)
    s2 = customtkinter.CTkSlider(my_w, orient="horizontal", from_= 5, to=100, command= slide_hor)
    s2.grid(row=5, column=1)
    
    







def upload_logo():
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    logo_path = filedialog.askopenfilename(filetypes=f_types)
    img =Image.open(filename1).convert("RGBA")
    logo=Image.open(logo_path).convert("RGBA") 
    logo=logo.resize((50,50))
    img=img.resize((300,300))
    img.paste(logo, (240, 240))
    img=ImageTk.PhotoImage(img)
   
    a1 =tk.Label(my_w)
    a1.grid(row=3,column=1)
    a1.image = img
       
    a1['image']=img 


def slide_ver(var):
    
    img =Image.open(filename1).convert("RGBA")
    logo =Image.open(logo_path).convert("RGBA")
    logo=logo.resize((int(s2.get()),int(s1.get())))
    img=img.resize((300,300))
    img.paste(logo, (240, 240))
    img=ImageTk.PhotoImage(img)
   
    a1 =tk.Label(my_w)
    a1.grid(row=3,column=1)
    a1.image = img
       
    a1['image']=img 


def slide_hor(var):
    
    img =Image.open(filename1).convert("RGBA")
    logo =Image.open(logo_path).convert("RGBA")
    logo=logo.resize((int(s2.get()), int(s1.get())))
    img=img.resize((300,300))
    img.paste(logo, (240, 240))
    img=ImageTk.PhotoImage(img)
   
    a1 =tk.Label(my_w)
    a1.grid(row=3,column=1)
    a1.image = img
       
    a1['image']=img 
    

my_w.mainloop()  
