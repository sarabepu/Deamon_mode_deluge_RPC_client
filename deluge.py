import os
import base64
from deluge_client import DelugeRPCClient
import time


tInicial= time.time()
client = DelugeRPCClient('127.0.0.1', 58846, 'monitoria', 'monitoria')


client.connect()
print(client.connected)

path = "C:/Users/Profesor/Documents/monitoria/nueva/torrents/ubuntu.torrent"


opts = {}
opts['download_location'] = "C:/Users/Profesor/Documents/monitoria/nueva/destino"


f = open(path, 'rb')
filedump = base64.encodestring(f.read())
f.close()

filename = os.path.basename(path)


a=client.call('core.add_torrent_file',filename,filedump,opts)

tFinal= time.time()

print(tFinal-tInicial)
