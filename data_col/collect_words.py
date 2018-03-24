import os
import csv
import glob

wordsSQL = open("/home/ubuntu/scripts/load_db/word_count.sql", "w")

path = '/home/ubuntu/statistics'
for filename in glob.glob(os.path.join(path, 'fixed_*_count.txt')):
    shortFile = os.path.basename(filename)
    wordCount = open(filename, 'r')
    topLine = wordCount.readline()
    
    items = [x.strip() for x in topLine.split(',')]

    artist = items[1]
    genre = items[2]
    song = items[0]

    count = 0
    dummyLine = next(wordCount)
    count = int(next(wordCount))

    wordsSQL.write("INSERT INTO unique_words(word_count, song_name, artist_name) VALUES (\"" + str(count) + "\"," + "\"" + song + "\"," + "\"" + artist + "\");\n")
