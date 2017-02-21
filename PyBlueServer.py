#!/usr/bin/python
# -*- coding: utf-8 -*-
# programme de connexion avec appareil bluetooth
# CB CH4Process
##############################################################
# programme pour reception data en provenance serveur Bluetooth
# Bluetooth using PyBluez (with Python 2).
#################################################################

import bluetooth
#  mettre a jour adresse device
hostMACAddress = '00:1f:e1:dd:08:3d' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
try:
    client, clientInfo = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data) # Echo back to client
except:	
    print("Closing socket")
    client.close()
    s.close()
