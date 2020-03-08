import sqlite3

conn = sqlite3.connect('emaildb.sqlite') #create emaildb.sqlite if not exist
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue #filter data starts with From that filter the email senders
    pieces = line.split('@') #only need domain name since the purpose of this code is to find out which organazation sends the most emails
    org = pieces[1] #store data without @
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) # ? prevents email injection
    row = cur.fetchone()
#insert data filtered out from above process
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10' #filter out top 10 senders

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
