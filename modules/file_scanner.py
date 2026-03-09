import os
import sqlite3

DB="database.db"

SCAN_DIRS=[
"/var/www",
"/home",
"/tmp"
]

def scan():

    print("Scanning suspicious files")

    suspicious_ext=[
    ".php",
    ".phtml",
    ".php5",
    ".php7",
    ".sh"
    ]

    for d in SCAN_DIRS:

        if not os.path.exists(d):
            continue

        for root,dirs,files in os.walk(d):

            for file in files:

                path=os.path.join(root,file)

                for ext in suspicious_ext:

                    if file.endswith(ext):

                        if "uploads" in path or "tmp" in path:

                            print("Suspicious file:",path)

                            conn=sqlite3.connect(DB)
                            c=conn.cursor()

                            c.execute(
                            "INSERT INTO findings(type,location,description) VALUES(?,?,?)",
                            ("file",path,"Suspicious script location")
                            )

                            conn.commit()
                            conn.close()
