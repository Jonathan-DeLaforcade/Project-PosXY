# -*- coding: cp1252 -*-
from Tkinter import *
import socket
coords = (0, 0)
nbHistory = 1

def set_text(entry,text):
    entry.delete(0,END)
    entry.insert(0,text)
    return

def addHistory():
    global nbHistory
    ListBoxHistory.insert(END, str(nbHistory) + ": (X: " + str(coords[0]) + " | Y:" + str(coords[1]) + ")")
    nbHistory = nbHistory +1

def mouseClick(event):
    global coords
    if (event.x >= 8) & (event.y >= 8) & (event.x <= 398) & (event.y <= 398):
        coords = (event.x,event.y)
        set_text(PosXEdit,str(event.x))
        set_text(PosYEdit,str(event.y))
        print("Mouse position: (%s %s)" % (coords[0],coords[1]))
        canvas.coords(rectangle,coords[0]-6, coords[1]-6, coords[0]+6, coords[1]+6)

def ImportHistory():
    text = ListBoxHistory.get(ListBoxHistory.curselection())
    text = text.split(" ")
    HistoryPosX = int(text[2])
    HistoryPosY = int(text[4].split(":")[1].split(")")[0])
    canvas.coords(rectangle,HistoryPosX-6, HistoryPosY-6, HistoryPosX+6, HistoryPosY+6)
    
    set_text(PosXEdit,str(HistoryPosX))
    set_text(PosYEdit,str(HistoryPosY))

def EditBoxPos():
    EditPosX = int(PosX.get())
    EditPosY = int(PosY.get())
    if (EditPosX < 8):
        EditPosX = 8
    if (EditPosY < 8):
        EditPosY = 8
    if (EditPosX > 398):
        EditPosX = 398
    if (EditPosY > 398):
        EditPosY = 398
    
    set_text(PosXEdit,str(EditPosX))
    set_text(PosYEdit,str(EditPosY))
    canvas.coords(rectangle,EditPosX-6, EditPosY-6, EditPosX+6, EditPosY+6)

def EnvoiePos():
    
    AddServer= "192.160.100.134"
    NumPort= 55678
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address=(AddServer,NumPort)
    sock.settimeout(2)
    sock.connect(server_address)
    print 'Open socket'
    CoordX = round(((coords[0]/398.0)*100),2)
    CoordY = round(((coords[1]/398.0)*100),2)

    message=("SX" + str(CoordX)+ "Y" + str(CoordY)+"F")
    sock.sendall(message)
    
    reponse = sock.recv(80)
    print '>Reponse du Server =',reponse

    sock.close()

    
fenetre = Tk()

fenetre['bg']='bisque'
fenetre.title('Commande CMS')
fenetre.geometry('860x710')

FrameTitle = Frame(fenetre, borderwidth=2, relief=GROOVE, width=900, height=30, bg="Gray67")
FrameTitle.pack(side=TOP, padx=2, pady=2, ipadx=300)
Label(FrameTitle, text="Commande CMS | By Jonathan de Laforcade").pack(pady=8)


FrameMenu = LabelFrame(fenetre, text="Favoris", borderwidth=2, relief=GROOVE, width=300, height=815, bg="Gray67")
FrameMenu.pack(side=LEFT, padx=4, pady=4, ipadx=6, ipady=6)

FrameMenuHistory = Frame(FrameMenu, width=300, height=525, bg="Gray67")
FrameMenuHistory.pack(side=TOP, padx=4, pady=4, ipadx=6, ipady=6)

ListBoxHistory = Listbox(FrameMenuHistory, height=31)
ListBoxHistory.pack(side=BOTTOM, fill=X, padx=0.5, pady=0.5)


Boutton_Import = Button(FrameMenu, text="Import� des favoris", command=ImportHistory).pack(side=BOTTOM,fill=X,pady=1)
Boutton_AddHistory = Button(FrameMenu, text="Ajout� aux favoris", command=addHistory).pack(side=BOTTOM,fill=X,pady=1)

FramePos = LabelFrame(fenetre, text="Selection de la position", borderwidth=2, relief=GROOVE, width=500, height=500, bg="Gray47")
FramePos.pack(side=RIGHT, padx=4, pady=4, ipadx=2, ipady=2)

FramePosEditsLignes = Frame(FramePos, width=500, height=100, bg="Gray47")
FramePosEditsLignes.pack(side=TOP, padx=4, pady=4)

FramePosEditsLigne1 = Frame(FramePosEditsLignes, width=500, height=100, bg="Gray47")
FramePosEditsLigne1.pack(side=TOP, padx=4, pady=4)

FramePosEditsLigne2 = Frame(FramePosEditsLignes, width=500, height=100, bg="Gray47")
FramePosEditsLigne2.pack(side=TOP, padx=4, pady=4)

FramePosCanvas = Frame(FramePos, borderwidth=2, relief=GROOVE, width=400, height=400, bg="Gray47")
FramePosCanvas.pack(side=BOTTOM, padx=4, pady=4)

FramePosCanvasButtonLigne = Frame(FramePosCanvas, bg="Gray47")
FramePosCanvasButtonLigne.pack(side=BOTTOM, padx=4, pady=4,fill=X)

PosX = StringVar()
PosY = StringVar()

PosXLabel = Label(FramePosEditsLigne1, text="Position X: ", width=10, bg="Gray47").pack(padx=4,side=LEFT)
PosXEdit = Entry(FramePosEditsLigne1, textvariable=PosX, width=30)
PosXLabel = Label(FramePosEditsLigne2, text="Position Y: ", width=10, bg="Gray47").pack(padx=4,side=LEFT)
PosYEdit = Entry(FramePosEditsLigne2, textvariable=PosY, width=30)

Boutton_actualise = Button(FramePosEditsLignes, text="Actualis�", command=EditBoxPos).pack(pady=10,side=BOTTOM)

canvas = Canvas(FramePosCanvas, width=400, height=400, bg="Gray37")
rectangle = canvas.create_rectangle(0,0,12,12,fill="sky blue")

Button_Envoie_Pos = Button(FramePosCanvasButtonLigne, text="Envoyer", command=EnvoiePos).pack(pady=10,side=RIGHT)

canvas.bind("<Button-1>", mouseClick)
canvas.bind("<B1-Motion>", mouseClick)

PosXEdit.pack(side=LEFT)
PosYEdit.pack(side=LEFT)
canvas.pack(side=BOTTOM)

fenetre.mainloop()


