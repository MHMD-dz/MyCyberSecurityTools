#!/usr/bin/env python3
import socket
from IPy import IP


TOP_100_PORTS = [
    7, 9, 13, 21, 22, 23, 25, 26, 37, 53, 79, 80, 81, 88, 106, 110, 111,
    113, 119, 135, 139, 143, 144, 179, 199, 389, 427, 443, 444, 445, 465,
    513, 514, 515, 543, 544, 548, 554, 587, 631, 646, 873, 990, 993, 995,
    1025, 1026, 1027, 1028, 1029, 1110, 1433, 1720, 1723, 1755, 1900,
    2000, 2001, 2049, 2121, 2717, 3000, 3128, 3306, 3389, 3986, 4899,
    5000, 5009, 5051, 5060, 5101, 5190, 5357, 5432, 5631, 5666, 5800,
    5900, 6000, 6001, 6646, 7070, 8000, 8008, 8009, 8080, 8081, 8443,
    8888, 9100, 9999, 10000, 32768, 49152, 49153, 49154, 49155, 49156,
    49157,
]


def getBanner(sock):
    return sock.recv(1024)

def scan(target):
    convertedIp = ip_check(target)
    if convertedIp == None:
        return
    print('\n' + '(: scanning the target ' + str(target) + ' ')
    for port in TOP_100_PORTS:
        scanPort(convertedIp,port)

def ip_check(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        try:
            return socket.gethostbyname(ip)
        except socket.gaierror:
            print('[-] the hostname ' + str(ip) + ' could not be resolved :(')
            return None
def scanPort(ip,port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip,port))
        try:
            banner = getBanner(sock)
            text = banner.decode(errors='replace').strip()
            print('[+] open port ' + str(port) + ' : ' + str(text) )
        except:
            print('[-] open port ' + str(port)  )
        sock.close()
    except ConnectionRefusedError:
        pass
    except socket.timeout:
        pass
    except Exception as e:
        print(f'[!] Port {port} error: {e}')


target = input("Enter the target/s ip (split multiple with ',' ) : ")


if ',' in target:
    for ip_address in target.split(','):
        scan(ip_address.strip(' '))
else:
    scan(target)