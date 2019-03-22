import socket
AddServer=raw_input('Address du Server :')
NumPort =input('Numero Port =')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address=(AddServer,NumPort)
sock.connect(server_address)
print 'Open socket'
message = raw_input('Entrer le Message=')

sock.sendall(message)
reponse = sock.recv(80)
print '>Reponce du Server =',reponse

sock.close()
