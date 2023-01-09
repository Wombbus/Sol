# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 19:46:38 2023

@author: Owner
"""
from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("random countries and capitals")

countryText = Entry(root)
capitalText = Entry(root)
capitalText.place(relx = 0.5,rely = 0.2,anchor = CENTER)
countryText.place(relx = 0.5,rely = 0.3,anchor = CENTER)



lbl = Label(root)
lbl2 = Label(root)
lbl.place(relx = 0.5,rely = 0.4,anchor = CENTER)
lbl2.place(relx = 0.5,rely = 0.5,anchor = CENTER)

countryList=[""]
capitalList=[""]

def name() :
    country_name = Entry()
    

lbl3 = Label(root)
lbl4 = Label(root)
lbl3.place(relx = 0.7)

btn = Button(root,text="Display Country And City Name",command = name,bg = "blue",fg = "white")
btn.place(relx = 0.5,rely=0.4,anchor=CENTER)
btn2 = Button(root,text = "Display Country And City Name Randomly",bg = "blue",fg = "white")
btn2.place(relx=0.5,rely = 0.6,anchor=CENTER)

root.mainloop()
