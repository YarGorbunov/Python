DELETE FROM Tracks;
DELETE FROM Albums;
DELETE FROM Artists;

INSERT INTO Artists
VALUES
    (1, 'Metallica'),
    (2, 'Megadeth'),
    (3, 'Anthrax'),
    (4, 'Eric Clapton'),
    (5, 'ZZ Top'),
    (6, 'Van Halen'),
    (7, 'Lynyrd Skynyrd'),
    (8, 'AC/DC'),
    (9, 'The Beatles');

INSERT INTO Albums (id_a, author, name, year)
VALUES
    (1, 1, '...And Justice For All',1988),
    (2, 1, 'Black Album',1991),
    (3, 1, 'Master of Puppets',1986),
    (4, 2, 'Endgame',2009),
    (5, 2, 'Peace Sells',1986),
    (6, 3, 'The Greater of 2 Evils',2004),
    (7, 4, 'Reptile',2001),
    (8, 4, 'Riding with the King',2000),
    (9, 5, 'Greatest Hits',1992),
    (10, 6, 'Greatest Hits',2004),
    (11, 7, 'All-Time Greatest Hits',1975),
    (12, 8, 'Greatest Hits',2003),
    (13, 9, 'Sgt. Pepper''s Lonely Hearts Club Band', 1967);

INSERT INTO Tracks (id_t, album, name)
VALUES
    (1,1,'One'),
    (2,1,'Blackened'),
    (3,2,'Enter Sandman'),
    (4,2,'Sad But True'),
    (5,3,'Master of Puppets'),
    (6,3,'Battery'),
    (7,4,'Dialectic Chaos'),
    (8,4,'Endgame'),
    (9,5,'Peace Sells'),
    (10,5,'The Conjuring'),
    (11,6,'Madhouse'),
    (12,6,'I am the Law'),
    (13,7,'Reptile'),
    (14,7,'Modern Girl'),
    (15,8,'Riding with the King'),
    (16,8,'Key to the Highway'),
    (17,9,'Sharp Dressed Man'),
    (18,9,'Legs'),
    (19,10,'Eruption'),
    (20,10,'Hot For Teacher'),
    (21,11,'Sweet Home Alabama'),
    (22,11,'Free Bird'),
    (23,12,'Thunderstruck'),
    (24,12,'T.N.T'),
    (25,13,'Sgt. Pepper''s Lonely Hearts Club Band'),
    (26,13,'With a Little Help from My Friends'),
    (27,13,'Lucy in the Sky with Diamonds'),
    (28,13,'Getting Better'),
    (29,13,'Fixing a Hole'),
    (30,13,'She''s Leaving Home'),
    (31,13,'Being for the Benefit of Mr. Kite!'),
    (32,13,'Within You Without You'),
    (33,13,'When I''m Sixty-Four'),
    (34,13,'Lovely Rita'),
    (35,13,'Good Morning Good Morning'),
    (36,13,'Sgt. Pepper''s Lonely Hearts Club Band (Reprise)'),
    (37,13,'A Day in the Life');