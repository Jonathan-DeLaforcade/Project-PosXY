#!/usr/bin/python
import socket
import serial
buf=1024
AddIP="192.160.100.134"
NumPort=55678
server_address = (AddIP, NumPort)
port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)


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
        port.write("\r\nSay something:")
	RepServeur = "OK"
        connection.sendall(RepServeur)
    finally:
        # Clean up the connection
        connection.close()

