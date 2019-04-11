from utorrentapi import UTorrentAPI, TorrentListInfo


apiclient = UTorrentAPI('http://localhost:7070/gui', 'monitoria', 'monitoria')
data = apiclient.get_list()
tor_list = TorrentListInfo(data)
add_file(file_path)
print(data['torrents'])