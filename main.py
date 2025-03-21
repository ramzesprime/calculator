import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from tkinter import PhotoImage

root = tk.Tk()
root.title("calculator")
root.geometry("250x200")



class Interface:
    def __init__(self):
        self.idbut = 0
        self.input1 = tk.StringVar()
        self.input2 = tk.StringVar()
    def input_labels(self):
        
        label = tk.Label(text="CALCULATOR 2000")
        label.grid(row=0,column=0)
        
        enter1 = tk.Entry(textvariable=self.input1)
        enter1.grid(row=2,column=0)
        
        enter2 = tk.Entry(textvariable=self.input2)
        enter2.grid(row=3,column=0)
        
        btnpls = tk.Button(text="+",command=self.plus)
        btnpls.grid(row=5,column=0)
        
        btnmi = tk.Button(text="-",command=self.minos)
        btnmi.grid(row=6,column=0)
        
        btnmlt = tk.Button(text="*",command=self.mlt)
        btnmlt.grid(row=5,column=1)
        
        btndev = tk.Button(text="/",command=self.dev)
        btndev.grid(row=6,column=1)
        
    def check(self):
        try:
            num1 = int(self.input1.get())
            num2 = int(self.input2.get())
            
            return num1, num2
        except ValueError:
            messagebox.showerror("eror", "enter valid nums")
            return None, None
        
           
            
        
    def plus(self):
        num1,num2 = self.check()
        messagebox.showinfo("GOOD BOI",num1+num2)
    def minos(self):
        num1,num2 = self.check()
        messagebox.showinfo("AMAZING",num1-num2)
    def mlt(self):
        num1,num2 = self.check()
        messagebox.showinfo("INCREBIBKAE",num1*num2)
    def dev(self):
        num1,num2 = self.check()
        try:
            messagebox.showinfo("SEXYT",num1/num2)
        except ZeroDivisionError:
            messagebox.showinfo("SEXYT","divison by zero")
            
    

sex = Interface()
sex.input_labels()
root.mainloop()