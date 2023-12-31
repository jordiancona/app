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
        self.entries = {}
        self.statustxt = ""
        self.Initialize()
        
    def Initialize(self):
        self.root = tk.Tk()
        self.root.title(self.titletxt)
        self.root.geometry("300x300")
        self.status = StringVar(value = self.statustxt)

        self.framerun = Frame()
        self.framerun.pack(expand = TRUE)
        self.frameSettings = Frame()
        self.frameSettings.pack(expand = TRUE)
        self.frameInformation = Frame()
        self.frameInformation.pack(expand = TRUE)
        self.framequit = Frame()
        self.framequit.pack(expand = TRUE)
        self.frameParameters = Frame()
        self.frameParameters.pack(expand = TRUE)

        # Run
        self.buttonrun = Button(self.framerun, text = "Run", width = 20, height = 2, command = self.Plotprofiles)
        self.buttonrun.pack(side = TOP, padx = 0, pady = 5)

        # Quit
        self.buttonquit = Button(self.framequit, text = "Quit", width = 20, height = 2, textvariable = "Cancel", command = self.Quit)
        self.buttonquit.pack(side = TOP, padx = 0, pady = 5)

        # Parameters
        for parameter in self.parameters:
            can = Canvas(self.frameParameters)

            lab = Label(can, width = 25, height = 1, text = parameter.__name__+"", anchor = W, takefocus = 0)
            lab.pack(side = 'left')

            ent = Entry(can, width = 11)
            ent.insert(0, str(parameter()))
            ent.pack(side = 'left')

            can.pack(side = 'top')

            self.entries[parameter] = ent
            
    def setStatusStr(self,newStatus):
            self.statusStr = newStatus
            self.status.set(self.statusStr)

    def NFW(self, r):
        a = 1
        rho0 = 0.5
        return rho0/((r/a)**1*(1+r/a)**2)
            
    def Plotprofiles(self):
        self.fig = plt.Figure()
        r = np.linspace(0,4,101)
        #self.fig.canvas.manager.window.update()
        plt.plot(r, NFW(r), lw = 0.5)
        plt.show()

    def Start(self):
        self.root.mainloop()

    def Quit(self):
        plt.close("all")
        self.root.quit()
        self.root.destroy()

    def SaveParameters(self):
        for parameter in parameters:
            parameter(float(self.entries[parameter].get()))
            self.setStatus
