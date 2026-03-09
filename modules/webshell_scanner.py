import os
import sqlite3

DB="database.db"

SCAN_DIRS=[
"/var/www",
"/home",
"/tmp"
]

def save(file,desc):

    conn=sqlite3.connect(DB)
    c=conn.cursor()

    c.execute(
    "INSERT INTO findings(type,location,description) VALUES(?,?,?)",
    ("webshell",file,desc)
    )

    conn.commit()
    conn.close()

def load_signatures():

    sig=[]

    with open("signatures.txt") as f:
        for line in f:
            line=line.strip()
            if line:
                sig.append(line)

    return sig

def scan():

    print("Scanning webshell signatures")

    sigs=load_signatures()

    for d in SCAN_DIRS:

        if not os.path.exists(d):
            continue

        for root,dirs,files in os.walk(d):

            for file in files:

                path=os.path.join(root,file)

                if not file.endswith((".php",".phtml",".php5",".php7",".js")):
                    continue

                try:

                    if os.path.getsize(path)>2000000:
                        continue

                    with open(path,"r",errors="ignore") as f:

                        for line in f:

                            for sig in sigs:

                                if sig in line:

                                    print("Webshell indicator:",path)

                                    save(path,sig)

                                    raise StopIteration

                except StopIteration:
                    continue

                except:
                    pass
