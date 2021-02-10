import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks2')
cur .execute('CREATE TABLE Tracks2 (title TEXT, plays INTEGER)')

conn.close()
                        
