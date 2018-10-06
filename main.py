from bot import TorrBot
import libtorrent as lt
import os
import sys
import time


def convertManget(magnet):
    sess = lt.session()
    prms = {
        'save_path': os.path.abspath(os.path.curdir),
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


def main():
    bot = TorrBot()
    name = input("Enter a movie name -\n")
    bot.getUrl(name)
    bot.query()
    magnets = bot.getMagnets()
    
    if magnets is not None:
        print("Top 5 searches: ")
        for i in range(len(magnets)):
            print("{0}. {1}".format(i+1, magnets[i]['title']))

        willDownload = input("Would you like to continue download")
        if willDownload == 'y':
            magnetNumber = int(input("Choose which one to be downloaded -\n"))
            magnetLink = magnets[magnetNumber-1]['magnet']
            filename = convertMagnet(magnetLink)
        else:
            anotherMovie = input("Would you like to download another movie - \n")
            if anotherMovie == 'y':
                main()
            else:
                print("Process terminated")
    else:
        print("No result found. Item is unavailable")


if __name__ == '__main__':
    main()

