import os
import sqlite3

DB="database.db"

def scan():

    print("Scanning processes")

    procs=os.popen("ps aux").read().splitlines()

    sig=[
    "bash -i",
    "nc ",
    "netcat",
    "perl -e",
    "python -c"
    ]

    for p in procs:

        for s in sig:

            if s in p:

                print("Suspicious process:",p)

                conn=sqlite3.connect(DB)
                c=conn.cursor()

                c.execute(
                "INSERT INTO findings(type,location,description) VALUES(?,?,?)",
                ("process",p,"Suspicious process")
                )

                conn.commit()
                conn.close()
