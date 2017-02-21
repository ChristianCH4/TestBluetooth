#!/usr/bin/python
# -*- coding: utf-8 -*-
# programme de connexion avec appareil bluetooth
# CB CH4Process

import bluetooth

# appareil recherché
target_name = "Ipad de Christian"
target_address = "FC:FC:48:60:CC:C7"

# recherche
nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print "appareil bluetooth trouvé avec adresse ", target_address
else:
    print "aucun appareil bluetooth trouvé avec cette adresse"
