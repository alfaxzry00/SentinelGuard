import os
import sqlite3

DB="database.db"

SCAN_DIRS=[
"/var/www",
"/home"
]

def scan():

    print("Scanning dangerous permissions")

    for d in SCAN_DIRS:

        result=os.popen(f"find {d} -type f -perm 777 2>/dev/null").read().splitlines()

        for r in result:

            print("777 permission:",r)

            conn=sqlite3.connect(DB)
            c=conn.cursor()

            c.execute(
            "INSERT INTO findings(type,location,description) VALUES(?,?,?)",
            ("permission",r,"777 permission")
            )

            conn.commit()
            conn.close()
