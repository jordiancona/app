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
        self.frameInformation = Frame()
        self.frameInformation.pack(expand = TRUE)
        self.framequit = Frame()
        self.framequit.pack(expand = TRUE)

        # Run
        self.buttonrun = Button(self.framerun, text = "Run", width = 20, height = 2, command = self.Plotprofiles)
        self.buttonrun.pack(side = TOP, padx = 0, pady = 5)

        #Quit
        self.buttonquit = Button(self.framequit, text = "Quit", width = 20, height = 2, textvariable = "Cancel", command = self.Quit)
        self.buttonquit.pack(side = TOP, padx = 0, pady = 5)
        
        self.nfw_var = IntVar()
        self.hernq_var = IntVar()
        self.nfw = Checkbutton(self.frameSettings, text = "NFW", variable = self.nfw_var)
        self.nfw.pack(side = TOP, padx = 5, pady = 5)

        self.hernquist = Checkbutton(self.frameSettings, text = "Hernquist", variable = self.hernq_var)
        self.hernquist.pack(side = TOP, padx = 10, pady = 5)

        self.parameters = [self.nfw, self.hernquist]
            
    def Plotprofiles(self, parameters):
        fig = plt.Figure()        
        self.fig.canvas.manager.window.update()
        for profile in self.parameters:
            if profile.get() == 1:
                
        plt.show()

    def Start(self, func = []):
        self.root.mainloop()

    def Quit(self):
        plt.close("all")
        self.root.quit()
        self.root.destroy()

    def Dehnen(self):
        pass        
