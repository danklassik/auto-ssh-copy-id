#!/usr/bin/python3
import os
import getpass
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u','--user', action='store', help='username')
parser.add_argument('-p','--port', action='store', default='22', help='port')
parser.add_argument('-L','--list', action='store', help='file list of IPs')
parser.add_argument('-i','--ip-address', action='store', nargs='+', metavar='host')

args = parser.parse_args()

if not args.user:
    print("Enter user name!")


if args.list:
    ips = [i for i in open(args.list, 'r').readlines()]
    passwd = getpass.getpass('Password: ')

    for ip in ips:
        cmd = 'ssh-copy-id {0}@{1} -p {2}'.format(args.user,ip,args.port)
        os.system('sshpass -p ' + passwd + ' ' + cmd)
        print("Key added: ", ip)

elif args.host:
    ip = args.host
    cmd = 'ssh-copy-id {0}@{1} -p {2}'.format(ip,args.port,passwd)
    os.system('sshpass -p ' + passwd + ' ' + cmd)
    print("Key added: ", ip)
else:
    print("No IP addresses were given to run script...")
