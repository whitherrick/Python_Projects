
import sqlite3

conn = sqlite3.connect('assignment1.db')

with conn:
    cur = conn.cursor()
    #creates the table if there is not one already
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_docname TEXT)")
    conn.commit()

conn = sqlite3.connect('assignment1.db')

#tuple of documents to add
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#loops through each to determine if it is a .txt file
for x in fileList:
    if x.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_docname) VALUES (?)", (x,))
            print(x)
conn.close()
