# SentinelGuard

SentinelGuard adalah tool keamanan Linux ringan untuk mendeteksi:

- backdoor
- webshell
- cronjob malware
- suspicious process
- hidden user
- dangerous permission
- suspicious open port

Tool ini dibuat untuk server kecil seperti VPS 1GB RAM.

## Features

Full security scan

Webshell detection

Cronjob malware detection

Suspicious process detection

Hidden root user detection

Permission audit

Network port scan

## Installation

Install python:

sudo apt install python3

Download repository:

git clone https://github.com/alfaxzry00/SentinelGuard

Masuk folder:

cd SentinelGuard

Jalankan tool:

chmod +x run.sh

./run.sh

## Directory scanned

SentinelGuard hanya scan folder penting:

/var/www  
/home  
/tmp  
/var/tmp  
/opt  
/usr/local

Folder sistem seperti berikut **tidak discan** agar server tetap ringan:

/proc  
/sys  
/dev  
/run  

## Warning

Tool ini dibuat untuk pembelajaran security dan basic detection.
