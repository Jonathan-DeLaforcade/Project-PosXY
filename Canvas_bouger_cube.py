# -*- coding: cp1252 -*-
from Tkinter import *

coords = (0, 0)

def mouseClick(event):
    global coords
    if (event.x >= 0) & (event.y >= 0) & (event.x <= 250) & (event.y <= 250):
        coords = (event.x,event.y)
        print("Mouse position: (%s %s)" % (coords[0], coords[1]))
        canvas.coords(rectangle, coords[0], coords[1], coords[0]+15, coords[1]+15)

fenetre = Tk()

canvas = Canvas(fenetre, width=250, height=250, bg="ivory")
rectangle = canvas.create_rectangle(0,0,15,15,fill="violet")

canvas.bind("<Button-1>", mouseClick)
canvas.bind("<B1-Motion>", mouseClick)
canvas.pack()

fenetre.mainloop()
