import sqlite3
import io
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()


def backupdb():
    b_conn=sqlite3.connect('backupdatabase.db')
    conn.backup(b_conn)
    b_conn.close()

backupdb()
c.close()

print(' Backup performed successfully!')
print(' Data Saved as backupdatabase.db')

conn.close()
