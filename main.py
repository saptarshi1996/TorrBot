from bot import TorrBot
from coverter import Converter
from downloader import Downloader
import sys
import os

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

        willDownload = int(input("\n\n1. Would you like to continue download\n2. Exit\n\n"))
        
        if willDownload == 1:
            magnetNumber = int(input("\n\nChoose which one to be downloaded -\n\n"))
            magnetLink = magnets[magnetNumber-1]['magnet']

            converter = Converter()
            filename = converter.convertManget(magnetLink)

            print("\n\n{0} has been downloaded in your current directory".format(filename))

            willDownloadFile = int(input("\n\n1. Download the file. \n2. Keep the .torrent file and exit \n3. Delete .torrent and exit\n\n"))
            
            if willDownload == 1:
                download_movie = Downloader()
                download_movie.downloadByName(filename)
                os.unlink(filename)
                
            elif willDownloadFile == 2:
                sys.exit(0)

            else:
                print("Deleted {0}".format(filename))
                os.unlink(filename)
                sys.exit(0)

        else:
            anotherMovie = int(input("\n\n1. Download another movie \n2. Exit\n\n"))
            if anotherMovie == 1:
                main()
            else:
                print("\n\nProcess terminated\n\n")
                sys.exit(0)
    else:
        print("\n\nNo result found. Item is unavailable\n\n")
        sys.exit(0)


if __name__ == '__main__':
    main()
