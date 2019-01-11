fichier = open("data.txt", "a")
for i in range(16):
    fichier.write("L"+str(i)+"\n")
fichier.close()

fichier = open("data.txt", "r")
lignes = fichier.readlines()
fichier.close()

for ligne in lignes:
    print ligne
