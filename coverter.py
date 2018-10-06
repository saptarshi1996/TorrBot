import libtorrent as lt
import os
import sys
import time


class Converter:
    def convertManget(self, magnet):
        sess = lt.session()
        prms = {
            'save_path': './',
            'paused': False,
            'auto_managed': False,
            'upload_mode': True
        }
        torr = lt.add_magnet_uri(sess, magnet, prms)
        dots = 0
        while not torr.has_metadata():
            dots += 1
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(1)
        if (dots): sys.stdout.write('\n')
        sess.pause()
        tinf = torr.get_torrent_info()
        fname = tinf.name() + '.torrent'
        f = open(fname, 'wb')
        f.write(lt.bencode(lt.create_torrent(tinf).generate()))
        f.close()
        sess.remove_torrent(torr)
        return fname

