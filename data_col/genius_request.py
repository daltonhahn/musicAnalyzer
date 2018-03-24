from bs4 import BeautifulSoup
import requests
import sys
import csv

urlFile = csv.reader(open(sys.argv[1], 'r'))
songArtist = csv.reader(open(sys.argv[2], 'r'))

for url_row, artist_row in zip(urlFile, songArtist):
    URL = url_row[0]
    page = requests.get(URL)
    html = BeautifulSoup(page.text, "html.parser")
    lyrics = html.find("div", class_="lyrics").get_text()
    lyricWriter = open('/home/ubuntu/lyrics/' + artist_row[1] + '.txt', 'w+')
    lyricWriter.write(artist_row[1] + "," + artist_row[0] + "," + artist_row[2] +"\n")
    lyricWriter.write(str(lyrics))
