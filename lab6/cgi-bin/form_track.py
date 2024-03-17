import cgi
import sqlite3

form = cgi.FieldStorage()
name = form.getfirst("tr_name")
album = form.getfirst("tr_album")
if album:
    album = int(album)
con = sqlite3.connect("music.db")
cur = con.cursor()

if all((name, album)):
    query = f"INSERT INTO Tracks (name, album) VALUES ('{name}', {album})"
    cur.execute(query)
    con.commit()
con.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')