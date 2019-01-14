# 15.1 Relational Database

# Terminology

"""
Database
Relation or Table, contains tuples and attributes.
Tuple or row, represents an object and information about the object.
Attribute also column or field.
Python cleans up unstructured data.
SQL handles structured data by creating tables, retrieving data, inserting or deleting and update data.
"""

# 15.2 Using databases

# Database Model

# A database model or database schema is the structure or format of a database, described in a formal language
# supported by the databse management system.

# SQLite is built in Python so just import it directly.

# 15.3 Single Table CRUD

# Manipulation on SQL
# INSERT INTO tablename(field, field) VALUES(value, value)
# DELETE FROM users WHERE email='ted@umich.edu'
# UPDATE users SET coloumname='newvalues WHERE email='csev@umich.edu'
# SELECT * FROM Users WHERE email='dfadfsaf'
# The * means all rows.
# SELECT * FROM Users ORDER BY email

CREATE TABLE Users(
	name VARCHAR(128),
	email VARCHAR(128)
)

INSERT INTO Users(name, email) VALUES('e', 'e@email')

DELETE FROM Users WHERE name = 'a'

UPDATE Users SET name = 'f' WHERE email = 'c@email'

SELECT * FROM Users
* means all 

SELECT * FROM Users ORDER BY name

#15.4 Worked Example
emaildb.py
--------------
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
