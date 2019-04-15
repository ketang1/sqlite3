#!/usr/bin/env python3

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    con.cursor()
    cur = con.cursor()
    cur.execute("CREATE TABLE friends(id INTEGER PRIMARY KEY, name TEXT);")
    cur.execute("INSERT INTO friends(name) VALUES ('Tom');")
    cur.execute("INSERT INTO friends(name) VALUES ('Rebecca');")
    cur.execute("INSERT INTO friends(name) VALUES ('Jim');")
    cur.execute("INSERT INTO friends(name) VALUES ('Robert');")

    last_row_id = cur.lastrowid
    print("The last Id of the inserted row is {}".format(last_row_id))