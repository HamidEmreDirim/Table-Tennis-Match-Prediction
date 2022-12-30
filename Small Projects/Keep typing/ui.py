import tkinter as tk
import customtkinter


customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")




class AppUi:

    def __init__(self):


        self.window = customtkinter.CTk()
        self.window.title("Don't stop typing!")

        self.d = customtkinter.CTkLabel(self.window, text="")
        self.d.grid(row=0, column=0)

        self.top = customtkinter.CTkLabel(self.window, text="Start typing when you ready.")
        self.top.grid(row=0, column=1)

        self.topb = customtkinter.CTkLabel(self.window, text="Don't forget that if you stop typing for 5 seconds your text will be gone!", width=20)
        self.topb.grid(row=1, column=1)

        self.paragraph = tk.Text(self.window, bg="#3a8a92", width= 45, height=8, font=("Arial", 12, "italic"))
        self.paragraph.grid(row=2, column=1)
        self.paragraph.config(pady=20)

        self.d1 = customtkinter.CTkLabel(self.window, text="")
        self.d1.grid(row=3, column=2)

       




    def check_input(self, x):
        

        self.window.after(100, self.check_input, x)


    def count_down(self, count):
        self.time_label.config(text=count)
        if count > 0:
            self.window.after(1000, self.count_down, count - 1)

        

        
        
            
       

        
        

        self.window.mainloop()