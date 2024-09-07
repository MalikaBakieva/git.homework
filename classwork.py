import sqlite3


conn = sqlite3.connect('database.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS cityy (
    id INTEGER PRIMARY KEY,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    postcode TEXT NOT NULL
)
''')


cities = [
    (1, 'Delhi', 'India', '11111'),
    (2, 'Osaka', 'Japan', '22222'),
    (3, 'Tashkent', 'Uzbekistan', '33333'),
    (4, 'Tokyo', 'Japan', '44444'),
    (5, 'New York', 'USA', '55555'),
    (6, 'Moscow', 'Russia', '66666'),
    (7, 'Brazil', 'Brazil', '77777'),
    (8, 'Shakh', 'Uzbekistan', '88888'),
    (9, 'Paris', 'France', '99999'),
    (10, 'Samarkand', 'Uzbekistan', '10000')
]


cursor.executemany('INSERT INTO cityy (id, city, country, postcode) VALUES (?, ?, ?, ?)', cities)


cursor.execute('SELECT * FROM cityy WHERE country = "Japan"')
japan_cities = cursor.fetchall()
print("Cities in Japan:", japan_cities)


conn.commit()
conn.close()



import sqlite3


conn = sqlite3.connect('database.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
      TEXT NOT NULL,
    country TEXT NOT NULL,
    postcode TEXT NOT NULL
)
''')


cities = [
    (1, 'Delhi', 'India', '11111'),
    (2, 'Osaka', 'Japan', '22222'),
    (3, 'Tashkent', 'Uzbekistan', '33333'),
    (4, 'Tokyo', 'Japan', '44444'),
    (5, 'New York', 'USA', '55555'),
    (6, 'Moscow', 'Russia', '66666'),
    (7, 'Brazil', 'Brazil', '77777'),
    (8, 'Shakh', 'Uzbekistan', '88888'),
    (9, 'Paris', 'France', '99999'),
    (10, 'Samarkand', 'Uzbekistan', '10000')
]


cursor.executemany('INSERT INTO cityy (id, city, country, postcode) VALUES (?, ?, ?, ?)', cities)


cursor.execute('SELECT * FROM cityy WHERE country = "Japan"')
japan_cities = cursor.fetchall()
print("Cities in Japan:", japan_cities)


conn.commit()
conn.close()

