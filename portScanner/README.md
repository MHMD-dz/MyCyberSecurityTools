# Port Scanner

A simple TCP port scanner written in Python. Scans the top 100 most common ports on one or more targets, detects open ports, and grabs service banners when available.

## Features
- Scans the top 100 most common ports
- Accepts IPv4 addresses or hostnames (resolved via DNS)
- Supports multiple targets in one run (comma-separated)
- Attempts to grab service banners from open ports
- Handles unresolvable hosts and per-port errors gracefully
- 1-second timeout per port

## Requirements
- Python 3.6+
- IPy

Install dependencies:
pip install IPy

## Usage
python3 portscanner.py

You will be prompted for a target:
Enter the target/s ip (split multiple with ',' ) :

### Examples
Single IP: 192.168.1.10
Single hostname: scanme.nmap.org
Multiple targets: 192.168.1.10, scanme.nmap.org, example.com

### Sample Output
(: scanning the target scanme.nmap.org
[+] open port 22 : SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
[-] open port 80
[!] Port 443 error: [Errno 104] Connection reset by peer

## How It Works
1. Reads the target(s) from user input.
2. Validates each target as an IP with IPy; if invalid, resolves it as a hostname via socket.gethostbyname().
3. Iterates over TOP_100_PORTS and attempts a TCP connection to each.
4. On success, reads up to 1024 bytes and decodes the banner.
5. Reports the port as open (with banner if available), or classifies the failure.

## Limitations
- Only scans the hardcoded top 100 ports
- Single-threaded (sequential scan)
- IPv4 only
- No command-line arguments
- Banner grabbing may return partial data or nothing for services that wait for a client request (HTTP, HTTPS, etc.)


## Author
BENZINEB MOHAMMED