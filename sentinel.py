import sqlite3
from modules import webshell_scanner
from modules import file_scanner
from modules import cron_scanner
from modules import process_scanner
from modules import permission_audit
from modules import network_scan
from modules import user_scanner

DB="database.db"

def init_db():

    conn=sqlite3.connect(DB)
    c=conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS findings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    location TEXT,
    description TEXT
    )
    """)

    conn.commit()
    conn.close()

def show_findings():

    conn=sqlite3.connect(DB)
    c=conn.cursor()

    rows=c.execute("SELECT * FROM findings")

    for r in rows:
        print(r)

    conn.close()

def menu():

    print("")
    print("1 Full Security Scan")
    print("2 Webshell Scan")
    print("3 Suspicious File Scan")
    print("4 Cronjob Scan")
    print("5 Suspicious Process")
    print("6 Permission Audit")
    print("7 Network Check")
    print("8 Hidden User Scan")
    print("9 View Database Findings")
    print("0 Exit")
    print("")

    return input("Select: ")

def main():

    init_db()

    while True:

        choice=menu()

        if choice=="1":

            webshell_scanner.scan()
            file_scanner.scan()
            cron_scanner.scan()
            process_scanner.scan()
            permission_audit.scan()
            network_scan.scan()
            user_scan.scan()

        elif choice=="2":
            webshell_scanner.scan()

        elif choice=="3":
            file_scanner.scan()

        elif choice=="4":
            cron_scanner.scan()

        elif choice=="5":
            process_scanner.scan()

        elif choice=="6":
            permission_audit.scan()

        elif choice=="7":
            network_scan.scan()

        elif choice=="8":
            user_scan.scan()

        elif choice=="9":
            show_findings()

        elif choice=="0":
            break

if __name__=="__main__":
    main()
