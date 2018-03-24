import os
import csv
import glob

syllableSQL = open("/home/ubuntu/scripts/load_db/syllable.sql", "w")

path = '/home/ubuntu/statistics'
for filename in glob.glob(os.path.join(path, 'fixed_*_syllables.txt')):
    syllables = open(filename, 'r')
    topLine = syllables.readline()
    
    items = [x.strip() for x in topLine.split(',')]

    artist = items[1]
    genre = items[2]
    song = items[0]

    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    sevens = 0
    eights = 0
    nines = 0
    tens = 0
    for line in syllables:
        if(line[:-1] == '1'):
            ones = ones + 1
        elif(line[:-1] == '2'):
            twos = twos + 1
        elif(line[:-1] == '3'):
            threes = threes + 1
        elif(line[:-1] == '4'):
            fours = fours + 1
        elif(line[:-1] == '5'):
            fives = fives + 1
        elif(line[:-1] == '6'):
            sixes = sixes + 1
        elif(line[:-1] == '7'):
            sevens = sevens + 1
        elif(line[:-1] == '8'):
            eights = eights + 1
        elif(line[:-1] == '9'):
            nines = nines + 1
        elif(line[:-1] == '10'):
            tens = tens + 1

    syllableSQL.write("INSERT INTO syllables(song_name, artist_name, one_syll, two_syll, three_syll, four_syll, five_syll, six_syll," \
        "seven_syll, eight_syll, nine_syll, ten_syll) VALUES (\"" + song + "\",\"" + artist + "\"," + str(ones) + "," + str(twos) + "," + str(threes) + "," +
        str(fours) + "," + str(fives) + "," + str(sixes) + "," + str(sevens) + "," + str(eights) + "," + str(nines) + "," + str(tens) + ");\n")
