import libtorrent as lt
import time
import sys
import os


class Downloader:
    def downloadByName(self, name):
        ses = lt.session()
        info = lt.torrent_info(name)
        h = ses.add_torrent({'ti': info, 'save_path': '/home/saptarshi/torrents'})
        print ('starting', h.name())

        while (not h.is_seed()):
            s = h.status()
            print("Downloading = {0}%".format(s.progress*10000))
            time.sleep(1)
        print (h.name(), 'complete')
