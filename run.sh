#!/bin/bash

python3 /home/ubuntu/scripts/billboard_scrape.py

sed -i -e 's|/||g' /home/ubuntu/scripts/song_artist.csv
sed -i -e 's|\.||g' /home/ubuntu/scripts/song_artist.csv

python3 /home/ubuntu/scripts/get_lyric_urls.py song_artist.csv

mysql -u root music < /home/ubuntu/scripts/load_db/db_schema.sql
mysql -u root music < /home/ubuntu/scripts/load_db/genre.sql
mysql -u root music < /home/ubuntu/scripts/load_db/artist.sql
mysql -u root music < /home/ubuntu/scripts/load_db/song.sql

python3 /home/ubuntu/scripts/data_col/genius_request.py /home/ubuntu/scripts/urls.txt /home/ubuntu/scripts/song_artist.csv
python3 /home/ubuntu/scripts/data_col/clean_lyrics.py

sed -i -e '2s/?//g' /home/ubuntu/fixed/fixed_*.txt
sed -i -e '2s/,//g' /home/ubuntu/fixed/fixed_*.txt

python3 /home/ubuntu/scripts/data_col/test.py /home/ubuntu/fixed/fixed_*.txt
python3 /home/ubuntu/scripts/data_col/count_syllables.py

python3 /home/ubuntu/scripts/data_col/collect_syllables.py
python3 /home/ubuntu/scripts/data_col/collect_words.py

mysql -u root music < /home/ubuntu/scripts/load_db/word_count.sql
mysql -u root music < /home/ubuntu/scripts/load_db/syllable.sql
