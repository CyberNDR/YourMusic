from googlesearch import search
import pytube
from pytube import YouTube
import webbrowser
import shutil
import os
import time
import pyfiglet

Logo = pyfiglet.figlet_format("Music")
print("\n")
print("\n")
print(Logo)
print("\n")

def main():
    with open("searches.txt", "r") as searchesopen:
        searchesread = searchesopen.readlines()
    savedsongs = os.listdir(f"{os.getcwd()}\Songs")
    if savedsongs == "":
        print("You currently don't have any saved song.")
    else:
        print("------------")
        print("Saved Songs:")
        print("------------")
        savedsongslist = []
        z = 0
        while z < len(savedsongs):
            savedsongslist.append(savedsongs[z].replace(".mp3", ""))
            print(savedsongslist[z])
            z += 1
    print("\n")
    if len(searchesread) > 7:
        newsearchesfile = open("searches.txt", "w")
        newsearches = []
        newsearches.append(searchesread[2])
        newsearches.append(searchesread[3])
        newsearches.append(searchesread[4])
        newsearches.append(searchesread[5])
        newsearches.append(searchesread[6])
        newsearches.append(searchesread[7])
        j = 0
        while j < len(newsearches):
            newsearchesfile.write(newsearches[j])
            j += 1
    else:
        print("------------------")
        print("Previous Searches:")
        print("------------------")
        y = 0
        while y < len(searchesread):
            print(searchesread[y].strip("\n"))
            y += 1
    print("\n")

    def search_song():
        inputsearch = input("Input the song name: ")
        outputsearch = open("searches.txt", "a")
        outputsearch.write("\n" + inputsearch)
        query = "youtube" + inputsearch
        results = ""
        result = []
        for results in search(query, tld="co.in", num=1, stop=1, pause=2):
            result.append(results)
        link = result[0]
        song = pytube.YouTube(link)
        print("Song Found")
        print(f"Title: {song.title}")
        print(f"Publish Date: {song.publish_date.strftime('%Y-%m-%d')}")
        print(f"Duration: {int(song.length/60)}:{song.length%60}")
        mp3filename = song.title + ".mp3"
        song.streams.filter(abr="160kbps", progressive=False).first().download(filename=mp3filename)
        currentdirectory = f"{os.getcwd()}\{mp3filename}"
        destinationdirectory = f"{os.getcwd()}\Songs\{mp3filename}"
        shutil.move(currentdirectory, destinationdirectory)
        webbrowser.open(f"{os.getcwd()}\Songs\{mp3filename}")
        return main()

    def play_a_saved_song():
        savedsongsget = os.listdir(f"{os.getcwd()}\Songs")
        savedsongs = []
        g = 0
        while g < len(savedsongsget):
            savedsongs.append(savedsongsget[g].replace(".mp3", ""))
            g += 1
        if savedsongs == "":
            print("You currently have no saved song.")
        else:
            print("-------------------")
            print("Listing Saved Songs")
            print("-------------------")
            s = 0
            while s < len(savedsongs):
                print(f"Number {s} - {savedsongs[s]}")
                s += 1
            print("\n")
            inputplay = int(input("Input the number of the song you want to play: "))
            webbrowser.open(f"{os.getcwd()}\Songs\{savedsongsget[inputplay]}")
        return main()

    def delete_a_saved_song():
        savedsongsget = os.listdir(f"{os.getcwd()}\Songs")
        h = 0
        while h < len(savedsongsget):
            print("Number ", h, savedsongsget[h].replace(".mp3", ""))
            h += 1
        print("\n")
        inputdelete = int(input("Input the number of the song you want to delete: "))
        os.remove(f"{os.getcwd()}\Songs\{savedsongsget[inputdelete]}")
        return main()

    print("-------")
    print("Options")
    print("-------")
    print("[1] Search for a New Song")
    print("[2] Play a Saved Song")
    print("[3] Delete a Saved Song")
    print("\n")
    print("[99] Exit")
    process = input("--->")
    if process == "1":
        try:
            search_song()
        except KeyboardInterrupt:
            print("Command Cancelled.")
            time.sleep(2)
            main()
    elif process == "2":
        play_a_saved_song()
    elif process == "3":
        try:
            delete_a_saved_song()
        except KeyboardInterrupt:
            print("Command Cancelled.")
            time.sleep(2)
            main()
    elif process == "99":
        exit()
    else:
        print("Error, available options: 1, 2, 3, 99.")
        time.sleep(3)
        return main()

try:
    main()
except KeyboardInterrupt:
    print("Command Cancelled.")
    time.sleep(2)
    main()
except Exception as e:
    print("Errore Generico:")
    print(e)
