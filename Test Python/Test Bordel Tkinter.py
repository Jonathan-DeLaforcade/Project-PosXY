from Tkinter import *
from tkMessageBox import *

# Wiki:
# 
#   http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel

fenetre = Tk()

#pannedwindow
p = PanedWindow(fenetre, orient=HORIZONTAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
p.add(Label(p, text='Volet 1', background='blue', anchor=CENTER))
p.add(Label(p, text='Volet 2', background='white', anchor=CENTER) )
p.add(Label(p, text='Volet 3', background='red', anchor=CENTER) )
p.pack()

#frame
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)

Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

#labelframe
l = LabelFrame(fenetre, text="Titre de la frame", padx=20, pady=20)
l.pack(fill="both", expand="yes")

#label
champ_label = Label(fenetre, text="Salut !")
champ_label.pack()

Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)

#button
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(fill=X)

#fenetre de saisie
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()

#case a cocher
var_case = IntVar()
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()

#boutons radio
var_choix = StringVar()

choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()

#listbox
liste = Listbox(fenetre)
liste.pack(fill=X)
liste.insert(END, "Pierre")
liste.insert(END, "Feuille")
liste.insert(END, "Ciseau")

#spinbox
s = Spinbox(fenetre, from_=0, to=10)
s.pack()


#canvas
canvas = Canvas(fenetre, width=150, height=120, background='yellow')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
canvas.pack()

#scale
value = DoubleVar()
scale = Scale(fenetre, variable=value)
scale.pack()

#warning
showinfo('Titre 2', 'Tant pis...')
# Liste des alertes:
# showinfo()
# showwarning()
# showerror()
# askquestion()
# askokcancel()
# askyesno()
# askretrycancel()

#menubar

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)

menu1.add_command(label="Test sous menu 1")
menu1.add_command(label="Test sous menu 2")
menu1.add_command(label="Test sous menu 3")

menubar.add_cascade(label="Test Menu 1", menu=menu1)

fenetre.config(menu=menubar)

fenetre.mainloop()
