#!/usr/bin/env python3

import sqlite3 as lite

uId = 1
uPrice = 62300

conn = lite.connect('create_table3.db')

with conn:
    cur = conn.cursor()
    cur.execute('UPDATE cars SET price=? WHERE id=?', (uPrice, uId))

    print(f"Number of rows updated: {cur.rowcount}")
