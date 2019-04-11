from torf import Torrent

t= Torrent(path='C:/Users/Profesor/Documents/arquisoft', 
 trackers=['udp://tracker.openbittorrent.com:80/announce'],
            comment='This is a comment')
t.private = False
t.generate()
t.write('C:/Users/Profesor/Documents/monitoria/nueva/torrents/ultimo.torrent')