import sys
import os
from tkinter import messagebox
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
import pickle
import reportlab
import pdfkit
import tkinter as tk
import webbrowser
from tkinter import PhotoImage
from tkinter import * 
from tkinter.ttk import *
from win32api import GetSystemMetrics
from PIL import Image, ImageTk



top = Tk()

C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\LoginUI.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
top.mainloop
top.mainloop()