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
        self.statustxt = ""
        self.Initialize()
        
    def Initialize(self):
        self.root = tk.Tk()
        self.status = StringVar(value = self.statustxt)

        self.framerun = Frame()
        self.framerun.pack(expand = TRUE)
        self.frameSettings = Frame()
        self.frameSettings.pack(expand = TRUE)
        self.frameParameters = Frame()
        self.frameParameters.pack(expand = TRUE)
        self.frameInformation = Frame()
        self.frameInformation.pack(expand = TRUE)

        # Run
        self.buttonrun = Button(self.framerun, width = 30, height = 2, textvariable = "Pause", command = self.Plotprofiles)
        self.buttonrun.pack(side = TOP, padx = 5, pady = 5)
        
    def SaveParameters(self):
        alpha = t.get("1.0","end-1c")
        beta = t.get("1.0","end-1c")
        return alpha, beta
            
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
