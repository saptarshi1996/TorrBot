from bot import TorrBot
from coverter import Converter


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

            converter = Converter()
            filename = converter.convertManget(magnetLink)

            print("{0} has been downloaded in your current directory".format(filename))

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

