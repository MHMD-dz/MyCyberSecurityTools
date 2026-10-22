import portscanner


target = input("[+] Enter the target IP: ")
vulnDir = input("[+] Enter the file directory to match the banners with: ")

scanner = portscanner.PortScanner(target)

scanner.scan()

print('[+] scanning for vulnerabilities: ')

with open(vulnDir , 'r') as file:
    count = 0
    for banner in scanner.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner :
                print('[!!] VULNERABLE  BANNER : ' + banner + ' [*] ON PORT : ' + str(scanner.ports[count]))
        count += 1