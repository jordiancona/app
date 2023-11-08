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
        self.Initialize()
        
    def Initialize(self):
        self.root = tk.Tk()
        self.status

        self.framerun = Frame()
        self.framerun.pack(expand = TRUE)
        self.frameSettings = Frame()
        self.frameSettings.pack(expand = TRUE)
        self.frameParameters = Frame()
        self.frameParameters.pack(expand = TRUE)
        self.frameInformation = Frame()
        self.frameInformation.pack(expand = TRUE)

        # Run
        self.buttonrun = Button(self.framerun, width = 30, height = 2, textvariable = "Pause", command = self.Protprofiles)
        self.buttonrun.pack(side = TOP, padx = 5, pady = 5)
        
    def SaveParameters(self):
        alpha = t.get("1.0","end-1c")
        beta = t.get("1.0","end-1c")
        return alpha, beta
            
    def Plotprofiles(self, parameters):
        fig = plt.Figure()
        r = np.linspace(0, self.radio, 101)
        plt.show()

    def Start(self):
        self.root.mainloop()

    def Quit(self):
        plt.close("all")
        self.root.quit()
