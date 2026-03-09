import sqlite3

DB="database.db"

def scan():

    print("Scanning hidden users")

    with open("/etc/passwd") as f:

        for line in f:

            parts=line.split(":")

            user=parts[0]
            uid=int(parts[2])

            if uid==0 and user!="root":

                print("Suspicious root user:",user)

                conn=sqlite3.connect(DB)
                c=conn.cursor()

                c.execute(
                "INSERT INTO findings(type,location,description) VALUES(?,?,?)",
                ("user",user,"UID 0 user")
                )

                conn.commit()
                conn.close()
