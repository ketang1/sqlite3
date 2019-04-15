#!/usr/bin/env python3

import sqlite3 as lite

conn = lite.connect('create_table3.db')

with conn:
    conn.row_factory = lite.Row

    cur = conn.cursor()
    cur.execute('SELECT * FROM cars')

    rows = cur.fetchall()

    for row in rows:
        print(f"{row['id']} {row['name']} {row['price']}")