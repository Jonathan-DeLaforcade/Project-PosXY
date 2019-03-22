#!/usr/bin/python
import socket
buf=1024
AddIP=raw_input('Entrer @IP du Serveur TCP:')
NumPort =input ('Entrer le Num du PORT :')
server_address = (AddIP, NumPort)
 
socketserveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketserveur.bind(server_address)
socketserveur.listen(1)

while True:
    print "serveur actif"
    connection, client_address = socketserveur.accept()
    try:
        print 'Addresse Client', client_address
        Message = connection.recv(80)
        print 'Addresse Client', client_address,'| Message Recu :',Message
        RepServeur = raw_input('On repond :')
        connection.sendall(RepServeur)          
    finally:
        # Clean up the connection
        connection.close()
