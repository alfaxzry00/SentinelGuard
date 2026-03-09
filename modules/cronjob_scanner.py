import os
import sqlite3

DB="database.db"

def save(item):

    conn=sqlite3.connect(DB)
    c=conn.cursor()

    c.execute(
    "INSERT INTO findings(type,location,description) VALUES(?,?,?)",
    ("cron",item,"Suspicious cronjob")
    )

    conn.commit()
    conn.close()

def scan():

    print("Scanning cronjobs")

    cron=os.popen("crontab -l 2>/dev/null").read().splitlines()

    suspicious=[
    "wget",
    "curl",
    "bash -i",
    "nc ",
    "python -c"
    ]

    for c in cron:

        for s in suspicious:

            if s in c:

                print("Suspicious cron:",c)

                save(c)
