#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Sep 15, 2020 10:21:40 AM -0300  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global che50
    che50 = tk.IntVar()
    global che51
    che51 = tk.IntVar()
    global che52
    che52 = tk.IntVar()
    global che53
    che53 = tk.IntVar()
    global che54
    che54 = tk.IntVar()
    global che64
    che64 = tk.IntVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import NewOne
    NewOne.vp_start_gui()



