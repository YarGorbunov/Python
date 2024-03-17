import xml.etree.ElementTree as ET
import sqlite3
from bs4 import BeautifulSoup
#from xml.dom import minidom
import cgi

def _pretty_print(current, parent=None, index=-1, depth=0):
    for i, node in enumerate(current):
        _pretty_print(node, current, i, depth + 1)
    if parent is not None:
        if index == 0:
            parent.text = '\n' + ('\t' * depth)
        else:
            parent[index - 1].tail = '\n' + ('\t' * depth)
        if index == len(parent) - 1:
            current.tail = '\n' + ('\t' * (depth - 1))

form = cgi.FieldStorage()
table = form.getfirst("table")

root = ET.Element(table)
structure = ET.SubElement(root,'structure')
items = ET.SubElement(root,'items')

con = sqlite3.connect('music.db')
cur = con.cursor()

try:
    cur.execute(f'SELECT * FROM {table}')
except sqlite3.OperationalError as e:
    print('Content-type: text/html\n')
    print(e)
    exit(0)

for row in cur.fetchall():
    item = ET.SubElement(items, 'item')
    # cur.description - кортежи, где содержатся имена столбцов
    for i, column_name in enumerate(cur.description):
        column_value = row[i]
        column_element = ET.SubElement(item, column_name[0])
        column_element.text = str(column_value)

cur.execute(f"PRAGMA foreign_key_list({table})")
fkeys = cur.fetchall()
cur.execute(f"PRAGMA table_info({table})")
for row in cur.fetchall():
    column = ET.SubElement(structure, row[1])
    column_info = row[2] + " " + str(row[-1])
    for fk in fkeys:
        if fk[3] == row[1]:
            column_info += " " + fk[2] + " " + fk[4]
            break
    column.text = column_info

#xml_str = ET.dump(root)
# print(xml_str)
print("Content-type: text/html\n")

print(f"""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Exported address table</title>
        </head>
        <body>
            <textarea rows=50 cols=60>
{BeautifulSoup(ET.tostring(root, encoding='utf8'), "xml").prettify()}
      </textarea>
    """)

print("""</body>
        </html>""")

con.close()