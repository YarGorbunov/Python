import sqlite3

con = sqlite3.connect('music.db')
curs = con.cursor()

print("Content-type: text/html\n")

responce = ""
def convert_table(table_name):
    responce = "<table>"
    cols = curs.execute('PRAGMA table_info('+table_name+')').fetchall()
    responce += "<thead><tr>"
    for col in cols:
        responce += "<td>"+str(col[1])+"</td>"
    responce += "</tr></thead><tbody>"
    data = curs.execute('SELECT * FROM ' + table_name).fetchall()
    for row in data:
        responce += "<tr>"
        for el in row:
            responce += "<td>" + str(el) + "</td>"
        responce += "</tr>"
    responce += "</tbody></table>"
    return responce
responce += convert_table("Artists")
responce += convert_table("Albums")
responce += convert_table("Tracks")
print(responce)

con.close()