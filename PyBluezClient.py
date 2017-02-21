#!/usr/bin/python
# -*- coding: utf-8 -*-
# programme de connexion avec appareil bluetooth
# CB CH4Process
##############################################################
# programme pour envoi data evers client Bluetooth
# Bluetooth using PyBluez (with Python 2).
#################################################################PyBluez (with Python 2).


import bluetooth
#  mettre a jour adresse device
serverMACAddress = '00:1f:e1:dd:08:3d'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    text = raw_input() # Note change to the old (Python 2) raw_input
    if text == "quit":
    break
    s.send(text)
sock.close()
