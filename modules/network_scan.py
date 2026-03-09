import os
import sqlite3

DB="database.db"

def scan():

    print("Checking suspicious ports")

    data=os.popen("ss -tulpn").read().splitlines()

    bad_ports=["1337","4444","5555","6666"]

    for d in data:

        for p in bad_ports:

            if p in d:

                print("Suspicious port:",d)

                conn=sqlite3.connect(DB)
                c=conn.cursor()

                c.execute(
                "INSERT INTO findings(type,location,description) VALUES(?,?,?)",
                ("network",d,"Suspicious port")
                )

                conn.commit()
                conn.close()
