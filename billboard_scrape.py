from bs4 import BeautifulSoup
import requests
import sys
import csv
URL_list = ["https://www.billboard.com/charts/pop-songs", "https://www.billboard.com/charts/rock-songs","https://www.billboard.com/charts/country-songs","https://www.billboard.com/charts/alternative-songs","https://www.billboard.com/charts/r-b-hip-hop-songs"]

songCSV = open("song_artist.csv", "w")

artistSQL = open("/home/ubuntu/scripts/load_db/artist.sql", "w")
songSQL = open("/home/ubuntu/scripts/load_db/song.sql", "w")
genreSQL = open("/home/ubuntu/scripts/load_db/genre.sql", "w")

genreSQL.write("INSERT INTO genres(genre) VALUES (\"Pop\");\n")
genreSQL.write("INSERT INTO genres(genre) VALUES (\"Rock\");\n")
genreSQL.write("INSERT INTO genres(genre) VALUES (\"Country\");\n")
genreSQL.write("INSERT INTO genres(genre) VALUES (\"Alternative\");\n")
genreSQL.write("INSERT INTO genres(genre) VALUES (\"Hip Hop\");\n")

for URL in URL_list:
    page = requests.get(URL)
    html = BeautifulSoup(page.text, "html.parser")
    info =  html.findAll("div", class_="chart-row__title")
    artist = ""
    song = ""
    for i in range(0, len(info)):
        lineCounter = 0
        for line in info[i]:
            if(lineCounter == 3): # a frames
                if(line.get_text()[-1] == "\n"):
                    artist = line.get_text()[1:-1]
                else:
                    artist = line.get_text()[1:-2]
            elif(lineCounter == 1):
                song = line.get_text()
            lineCounter = lineCounter + 1
        if(URL == "https://www.billboard.com/charts/pop-songs"):
            songCSV.write("\"" + artist + "\"" + "," + "\"" + song + "\"" + "," + "Pop" + "\n")
            songSQL.write("INSERT IGNORE INTO songs(song_name, genre, artist) VALUES (\"" + song + "\"," + "\"Pop\",\"" + artist + "\");\n") 
        if(URL == "https://www.billboard.com/charts/rock-songs"):
            songCSV.write("\"" + artist + "\"" + "," + "\"" + song + "\"" + "," + "Rock" + "\n")
            songSQL.write("INSERT IGNORE INTO songs(song_name, genre, artist) VALUES (\"" + song + "\"," + "\"Rock\",\"" + artist + "\");\n") 
        if(URL == "https://www.billboard.com/charts/country-songs"):
            songCSV.write("\"" + artist + "\"" + "," + "\"" + song + "\"" + "," + "Country" + "\n")
            songSQL.write("INSERT IGNORE INTO songs(song_name, genre, artist) VALUES (\"" + song + "\"," + "\"Country\",\"" + artist + "\");\n") 
        if(URL == "https://www.billboard.com/charts/alternative-songs"):
            songCSV.write("\"" + artist + "\"" + "," + "\"" + song + "\"" + "," + "Alternative" + "\n")
            songSQL.write("INSERT IGNORE INTO songs(song_name, genre, artist) VALUES (\"" + song + "\"," + "\"Alternative\",\"" + artist + "\");\n") 
        if(URL == "https://www.billboard.com/charts/r-b-hip-hop-songs"):
            songCSV.write("\"" + artist + "\"" + "," + "\"" + song + "\"" + "," + "Hip Hop" + "\n")
            songSQL.write("INSERT IGNORE INTO songs(song_name, genre, artist) VALUES (\"" + song + "\"," + "\"Hip Hop\",\"" + artist + "\");\n") 
        artistSQL.write("INSERT IGNORE INTO artists(artist_name) VALUES (\"" + artist + "\");\n")
