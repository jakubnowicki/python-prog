import sqlite3

def init(cur):
    cur.execute('''CREATE TABLE stocks
                   (date text, trans text, symbol text, qty real, price real)''')

def add(cur, data, tranzakcja, firma, ilosc, cena):
    cur.execute("INSERT INTO stocks VALUES (?, ?, ?, ?, ?)", (data, tranzakcja, firma, ilosc, cena))

def main():
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    add(cur, '2011-01-05', 'SELL', 'ORA', 123, 4.99)

    for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

    con.commit()
    con.close()

if __name__ == '__main__':
    main()

#  ale są też ORMy :)
#     sqlalchemy
#     Django ORM