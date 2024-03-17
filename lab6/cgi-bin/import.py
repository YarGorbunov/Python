import xml.etree.ElementTree as ET
import sqlite3
#from xml.dom import minidom
import cgi

form = cgi.FieldStorage()
xml_string = form.getfirst("xml")

con = sqlite3.connect('music.db')
cur = con.cursor()

root = ET.fromstring(xml_string)
table = root.tag
columns = root.findall('structure')[0]
#columns = list(filter(lambda node: node.nodeType == 1, columns))
table_body = ""
fkeys = ""
for column in columns:
    table_body += column.tag
    column_info = column.text.split()
    table_body += " " + column_info[0]
    if column_info[1] == "1":
        table_body += " PRIMARY KEY"
    if column.tag == "id":
        table_body += " AUTOINCREMENT"
    table_body += ', '
    if len(column_info) == 4:
        fkeys += f"FOREIGN KEY ({column.tag}) REFERENCES {column_info[-2]} ({column_info[-1]}), "
table_body += fkeys
table_body = table_body[:-2]

cur.execute(f"CREATE TABLE IF NOT EXISTS {table} ( {table_body} );")
con.commit()

items = root.findall('items')[0]
#items = list(filter(lambda node: node.nodeType == 1, items))

print('Content-type: text/html\n')
for item in items:
    #item_columns = list(filter(lambda node: node.nodeType == 1, item.childNodes))
    item_columns = item
    column_names = ", ".join([item_column.tag for item_column in item_columns])
    column_values = list(map(lambda value: f'"{value.strip()}"', [item_column.text for item_column in item_columns]))
    column_values = ", ".join(column_values)
    print(f"INSERT INTO {table} ({column_names}) VALUES ({column_values});")
    cur.execute(f"INSERT INTO {table} ({column_names}) VALUES ({column_values});")
con.commit()

con.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')
