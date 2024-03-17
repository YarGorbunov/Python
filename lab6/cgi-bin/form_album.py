import cgi
import sqlite3

form = cgi.FieldStorage()
name = form.getfirst("al_name")
year = form.getfirst("al_year")
if year:
    year = int(year)
author = form.getfirst("al_author")
if author:
    author = int(author)
con = sqlite3.connect("music.db")
cur = con.cursor()

if all((name, year, author)):
    query = f"INSERT INTO Albums (name, year, author) VALUES ('{name}', {year}, {author})"
    cur.execute(query)
    con.commit()
con.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')