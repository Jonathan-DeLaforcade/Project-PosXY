# -*- coding: cp1252 -*-
from Tkinter import *

coords = (0, 0)

def set_text(entry,text):
    entry.delete(0,END)
    entry.insert(0,text)
    return

def mouseClick(event):
    global coords
    if (event.x >= 8) & (event.y >= 8) & (event.x <= 494) & (event.y <= 494):
        coords = (event.x,event.y)
        set_text(PosXEdit,str(event.x))
        set_text(PosYEdit,str(event.y))
        print("Mouse position: (%s %s)" % (coords[0],coords[1]))
        canvas.coords(rectangle, coords[0]-6, coords[1]-6, coords[0]+6, coords[1]+6)

fenetre = Tk()

fenetre['bg']='bisque'
fenetre.title('Commande CMS')
fenetre.geometry('850x660')

FrameTitle = Frame(fenetre, borderwidth=2, relief=GROOVE, width=900, height=30, bg="Gray82")
FrameTitle.pack(side=TOP, padx=2, pady=2, ipadx=300)
Label(FrameTitle, text="Commande CMS | By Jonathan de Laforcade & Quentin Balanant").pack(pady=8)


FrameMenu = LabelFrame(fenetre, text="Menu", borderwidth=2, relief=GROOVE, width=250, height=500, bg="Gray67")
FrameMenu.pack(side=LEFT, padx=4, pady=4)

FramePos = LabelFrame(fenetre, text="Selection de la position", borderwidth=2, relief=GROOVE, width=500, height=500, bg="Gray47")
FramePos.pack(side=RIGHT, padx=4, pady=4)

FramePosEditsLignes = Frame(FramePos, width=500, height=100, bg="Gray47")
FramePosEditsLignes.pack(side=TOP, padx=4, pady=4)

FramePosEditsLigne1 = Frame(FramePosEditsLignes, width=500, height=100, bg="Gray47")
FramePosEditsLigne1.pack(side=TOP, padx=4, pady=4)

FramePosEditsLigne2 = Frame(FramePosEditsLignes, width=500, height=100, bg="Gray47")
FramePosEditsLigne2.pack(side=TOP, padx=4, pady=4)

FramePosCanvas = Frame(FramePos, borderwidth=2, relief=GROOVE, width=500, height=500, bg="Gray47")
FramePosCanvas.pack(side=BOTTOM, padx=4, pady=4)

PosX = StringVar()
PosY = StringVar()

PosXLabel = Label(FramePosEditsLigne1, text="Position X: ", width=10, bg="Gray47").pack(padx=4,side=LEFT)
PosXEdit = Entry(FramePosEditsLigne1, textvariable=PosX, width=30)
PosXLabel = Label(FramePosEditsLigne2, text="Position Y: ", width=10, bg="Gray47").pack(padx=4,side=LEFT)
PosYEdit = Entry(FramePosEditsLigne2, textvariable=PosY, width=30)

canvas = Canvas(FramePosCanvas, width=500, height=500, bg="Gray37")
rectangle = canvas.create_rectangle(0,0,12,12,fill="sky blue")

canvas.bind("<Button-1>", mouseClick)
canvas.bind("<B1-Motion>", mouseClick)

PosXEdit.pack(side=LEFT)
PosYEdit.pack(side=LEFT)
canvas.pack(side=BOTTOM)

fenetre.mainloop()


