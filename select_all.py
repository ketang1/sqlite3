#!/usr/bin/env python3

import sqlite3 as lite

con = lite.connect('create_table3.db')

with con:

    cur = con.cursor()
    cur.execute('SELECT * FROM cars')

    rows = cur.fetchall()

    for row in rows:
        print(row)