import tkinter as tk
import customtkinter
from data import pharagraf_list


data_l = []
for x in pharagraf_list:
    data_l.append(x.split(" "))


customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")


class AppUi:

    def __init__(self):
        self.time = 60
        self.window = customtkinter.CTk()
        self.window.title('Type Speed Calculator')
        
        
        
        self.d = customtkinter.CTkLabel(self.window, text="")
        self.d.grid(row=0, column=0)

        self.l1 = customtkinter.CTkLabel(self.window, text="Try to type the paragraph as quick as possible", text_font="bold") 
        self.l1.grid(row=0, column=1)

        self.d = customtkinter.CTkLabel(self.window, text="")
        self.d.grid(row=0, column=2)

        self.i1 = customtkinter.CTkEntry(self.window, width=380, justify="center")
        self.i1.grid(row=2, column=1)

        self.time_label = tk.Label(self.window, text="60")
        self.time_label.grid(row=3, column=1)

        self.paragraph = tk.Text(self.window, bg="#3a8a92", width= 45, height=8, font=("Arial", 12, "italic"))
        self.paragraph.grid(row=1, column=1)
        

        self.start_timer("")
        self.update_text(0)


    def count_down(self, count):
        self.time_label.config(text=count)
        if count > 0:
            self.window.after(1000, self.count_down, count - 1)

    
    def start_timer(self, dt):
        if self.i1.get() != "":
            self.count_down(60)
            self.check_input(0, 0, 0, 0)
        else:       
            self.window.after(100, self.start_timer, dt)


    def check_input(self,start, xx, p_i, point):
        if int(self.time_label.cget("text")) > 0:
            if start < len(data_l[p_i]): 
                word_length = len(data_l[p_i][start])
                
                if xx == 0:    
                    self.paragraph.tag_add("start", "1.0",f"1.{word_length + start}")
                else:
                    self.paragraph.tag_add("start", "1.0",f"1.{xx + start}")

                self.paragraph.tag_configure("start", background="Yellow", foreground="black")
                if self.i1.get() == data_l[p_i][start]:
                    start += 1
                    point += len(self.i1.get())
                    self.i1.delete(0, last= word_length)
                    xx += word_length
                    

                self.window.after(100, self.check_input, start, xx, p_i, point)
            else:
                p_i +=1
                self.paragraph.tag_add("start", "1.0",f"1.{xx + start}")
                self.update_text(p_i)
                self.window.after(100, self.check_input, 0, 0, p_i, point)
        else:
            print(f"Time is up sob your point is {point} word per minute")
       
    def update_text(self,index):
        self.paragraph.delete('1.0', tk.END)
        for word in data_l[index]:
            self.paragraph.insert(tk.INSERT, word)
            self.paragraph.insert(tk.INSERT, " ")
        self.paragraph.insert(tk.END, "")
       
        self.window.mainloop()
