DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS unique_words;
DROP TABLE IF EXISTS syllables;

CREATE TABLE genres
(
  genre_id INT NOT NULL AUTO_INCREMENT,
  genre VARCHAR(20) UNIQUE NOT NULL,
  PRIMARY KEY(genre_id)
);

CREATE TABLE songs
(
  song_id INT NOT NULL AUTO_INCREMENT,
  song_name VARCHAR(100) NOT NULL,
  genre VARCHAR(20) NOT NULL,
  artist VARCHAR(100) NOT NULL,
  PRIMARY KEY(song_id)
);

CREATE TABLE artists
(
  artist_id INT NOT NULL AUTO_INCREMENT,
  artist_name VARCHAR(100) UNIQUE NOT NULL,
  PRIMARY KEY(artist_id, artist_name)
);

CREATE TABLE unique_words
(
  words_id INT NOT NULL AUTO_INCREMENT,
  word_count INT NOT NULL,
  song_name VARCHAR(100) NOT NULL,
  artist_name VARCHAR(100) NOT NULL,
  PRIMARY KEY(words_id)
);

CREATE TABLE syllables 
(
  syllable_id INT NOT NULL AUTO_INCREMENT,
  one_syll INT NOT NULL,
  two_syll INT NOT NULL,
  three_syll INT NOT NULL,
  four_syll INT NOT NULL,
  five_syll INT NOT NULL,
  six_syll INT NOT NULL,
  seven_syll INT NOT NULL,
  eight_syll INT NOT NULL,
  nine_syll INT NOT NULL,
  ten_syll INT NOT NULL,
  song_name VARCHAR(100) NOT NULL,
  artist_name VARCHAR(100) NOT NULL,
  PRIMARY KEY(syllable_id)
);
