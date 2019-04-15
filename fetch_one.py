#!/usr/bin/env python3

import sqlite3 as lite

conn = lite.connect('create_table3.db')

with conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM cars')

    while True:
        row = cur.fetchone()

        if not row:
            break
        
        print(row[0], row[1], row[2])