import sys
import os
import glob

path = '/home/ubuntu/lyrics'
for filename in glob.glob(os.path.join(path, '*.txt')):
    shortFile = os.path.basename(filename)
    print(shortFile)
    lyricReader = open(filename, 'r') 
 
    finalWrite = open("/home/ubuntu/fixed/fixed_" + shortFile, 'w') 
 
    for line in lyricReader: 
        if(line[0] != '['): 
            finalWrite.write(line)
