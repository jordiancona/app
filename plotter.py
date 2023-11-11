#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import numpy as np

try :
    from tkinter import *
    import tkinter as tk
    from tkinter import ttk

except:
    print("tkinter not found.")

class Plotter:
    def __init__(self, title = "DM Plotter", parameters = []):
        self.titletxt = title
        self.parameters = parameters
        self.statustxt = "Hello"
        self.Initialize()
        
    def Initialize(self):
        self.root = tk.Tk()
        self.root.title(self.titletxt)
        self.root.geometry("350x350")
        self.status = StringVar(value = self.statustxt)

        self.framerun = Frame()
        self.framerun.pack(expand = TRUE)
        self.frameSettings = Frame()
        self.frameSettings.pack(expand = TRUE)
        self.frameParameters = Frame()
        self.frameParameters.pack(expand = TRUE)
        self.frameInformation = Frame()
        self.frameInformation.pack(expand = TRUE)

        self.alpha = Entry(self.root, width = 10)
        self.alpha.pack()
        # Run
        self.buttonrun = Button(self.framerun, text = "Run", width = 20, height = 2, textvariable = "Pause", command = self.Plotprofiles)
        self.buttonrun.pack(side = BOTTOM, padx = 5, pady = 5)
            
    def Plotprofiles(self, parameters):
        fig = plt.Figure()
        self.DrawFunc(parameters)
        self.fig.canvas.manager.window.update()
        plt.show()

    def Start(self, func = []):
        if len(func) == 3:
            self.InitcFunc = func[0]
            self.DrawFunc = func[1]
            self.InitcFunc()
            self.Plotprofiles()
        self.root.mainloop()

    def Quit(self):
        plt.close("all")
        self.root.quit()
        self.root.destroy()
