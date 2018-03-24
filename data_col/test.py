import sys
import codecs
import os
import glob


stopwords_file = '/home/ubuntu/scripts/data_col/stops.txt'
custom_stopwords = set(codecs.open(stopwords_file, 'r', 'utf-8').read().splitlines())

path = '/home/ubuntu/fixed'
for filename in glob.glob(os.path.join(path, '*.txt')):
    shortFile = os.path.basename(filename)
    fp = open(filename, 'r')
    topLine = fp.readline()

    words = fp.read().split()

    words = [word for word in words if len(word) > 1]
    words = [word for word in words if not word.isnumeric()]
    words = [word.lower() for word in words]
    words = [word for word in words if word not in custom_stopwords]

    unique = set(words)

    uniqueFile = open('/home/ubuntu/statistics/' + shortFile[:-4] + '_count.txt', 'w')
    uniqueFile.write(topLine + "\n")
    uniqueFile.write(str(len(unique)))
    uniqueFile.write("\n")

    uniqueWords = open('/home/ubuntu/statistics/' + shortFile[:-4] + '_words.txt', "w")
    uniqueWords.write(topLine + "\n")

    for word in unique:
        uniqueWords.write(word)
        uniqueWords.write("\n")
