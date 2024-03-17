CREATE TABLE IF NOT EXISTS Artists (
id_m INTEGER PRIMARY KEY,
name TEXT NOT NULL
);
               
CREATE TABLE IF NOT EXISTS Albums (
id_a INTEGER PRIMARY KEY,
name TEXT NOT NULL,
year INTEGER NOT NULL,
author INTEGER NOT NULL,
FOREIGN KEY(author) REFERENCES Artists(id_m)
);
               
CREATE TABLE IF NOT EXISTS Tracks (
id_t INTEGER PRIMARY KEY,
name TEXT NOT NULL,
album INTEGER NOT NULL,
FOREIGN KEY(album) REFERENCES Albums(id_a)
);