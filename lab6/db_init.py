import sqlite3

connection = sqlite3.connect('music.db')
cursor = connection.cursor()
cursor.executescript(open('db_creation.sql').read())
cursor.executescript(open('db_insertion.sql').read())
# Tracks and albums of Metallica
res = cursor.execute('''
SELECT 
    tr.name, al.name
FROM 
    Tracks tr
JOIN 
    Albums al ON album = al.id_a
JOIN 
    Artists ar ON author = ar.id_m
WHERE 
    ar.name = "Metallica";
''')
print(res.fetchall())
# Amount of Tracks in each Metallica Album
res = cursor.execute('''
SELECT 
    al.name, COUNT(*)
FROM 
    Tracks tr
JOIN 
    Albums al ON album = al.id_a
JOIN 
    Artists ar ON author = ar.id_m
WHERE 
    ar.name = "Metallica"
GROUP BY al.name;
''')
print(res.fetchall())
# Author of the oldest album
res = cursor.execute('''
SELECT 
    ar.name
FROM 
    Albums al
JOIN
    Artists ar ON al.author = ar.id_m
WHERE 
    al.year = (SELECT MIN(year) FROM Albums)
GROUP BY al.name;
''')
print(res.fetchall())