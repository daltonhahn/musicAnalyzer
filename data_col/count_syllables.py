import pyphen
import os
import glob

pyphen.language_fallback('nl_NL_variant1')
'nl_NL' in pyphen.LANGUAGES

dic = pyphen.Pyphen(lang='en_US')

path = '/home/ubuntu/statistics'
for filename in glob.glob(os.path.join(path, 'fixed_*_words.txt')):
    shortFile = os.path.basename(filename)
    words = open(filename, 'r')
    syllableWriter = open('/home/ubuntu/statistics/' + shortFile[:-9] + 'syllables.txt', 'w')
    topLine = words.readline()
    syllableWriter.write(topLine + "\n")

    for word in words:
        hyphenated = dic.inserted(word)    
        syllables = 1
        for letter in hyphenated:
            if(letter == '-'):
                syllables = syllables + 1
        syllableWriter.write(str(syllables))
        syllableWriter.write("\n")
