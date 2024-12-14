import sqlite3 
con = sqlite3.connect("youtube.db") # соединение с базой данных, если бд нет, то файл создастся

cur = con.cursor()
cur.execute("CREATE TABLE youtube(title, year, score)")
cur.execute("""
    INSERT INTO youtube VALUES
        ('video title', 1975, 8.2),
        ('And Now for Something Completely Different', '7.3)
""")
con.commit()

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

con.close()
con.commit()