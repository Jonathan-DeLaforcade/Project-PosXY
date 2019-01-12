# -*- coding: cp1252 -*-
from Tkinter import *


def login():
    User = UserPseudoEdit.get()
    Mdp = UserPasswordEdit.get()
    print "utilisateur " + User + " c'est connecté avec le mot de passe: " + Mdp

fenetre = Tk()
fenetre.title('Miguel le plus beau')
#fenetre.geometry('500')


L1 = Frame(fenetre, height=50, bg="Gray67")
L1.pack(side=TOP, padx=4, pady=1, fill=X)

Label(L1, text = "Design by Nirawin pour le con de minibosh", bg="Gray67").pack(side=TOP, pady=10)




L2 = Frame(fenetre, height=50)
L2.pack(side=TOP, padx=4, pady=1, fill=X)

Pseudo = StringVar()
Label(L2, text = "Pseudo:           ").pack(side=LEFT, pady=10)
UserPseudoEdit = Entry(L2, textvariable=Pseudo, width=30)


L3 = Frame(fenetre, height=50)
L3.pack(side=TOP, padx=4, pady=1, fill=X)

Mdp = StringVar()
Label(L3, text = "Mot de passe: ").pack(side=LEFT, pady=10)
UserPasswordEdit = Entry(L3, textvariable=Mdp, width=30)


L4 = Frame(fenetre, height=50)
L4.pack(side=TOP, padx=4, pady=1, fill=X)

Boutton_Validate = Button(L4, text="Login", command=login).pack(side=RIGHT,fill=X)

UserPseudoEdit.pack(side=LEFT)
UserPasswordEdit.pack(side=LEFT)






fenetre.mainloop()





