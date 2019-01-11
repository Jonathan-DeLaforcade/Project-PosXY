fichier = open("data.txt", "a")
for i in range(16):
    fichier.write("L"+str(i)+"\n")
fichier.close()

liste = []

fichier = open("data.txt", "r")

for i in range (0,10):
    liste.append(fichier.readline()) 

fichier.close()

    
for i in liste:
    print i
