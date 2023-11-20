
from tkinter import *
import plotter as ptr

alpha = 1
beta = 1

def Alpha(val = alpha):
    global alpha
    alpha = float(val)
    return val

def Beta(val = beta):
    global beta
    beta = float(val)
    return val

ptr.Plotter(parameters = [Alpha, Beta]).Start()
