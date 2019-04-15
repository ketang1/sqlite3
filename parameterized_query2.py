#!/usr/bin/env python3

import sqlite3 as lite

uId = 4

conn = lite.connect('create_table3.db')

with conn:
    cur = conn.cursor()
    cur.execute('SELECT name, price FROM cars WHERE id=:Id', {"Id": uId})

    row = cur.fetchone()
    print(row[0], row[1])
