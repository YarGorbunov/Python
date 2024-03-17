import cgi
import sqlite3

form = cgi.FieldStorage()
name = form.getfirst("ar_name")
con = sqlite3.connect("music.db")
cur = con.cursor()

if name:
    query = f"INSERT INTO Artists (name) VALUES ('{name}')"
    cur.execute(query)
    con.commit()
con.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')