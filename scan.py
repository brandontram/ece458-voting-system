import nmap, socket, fcntl, struct

def get_netmask(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x891b, struct.pack('256s',ifname))[20:24])

iface = "en1"
address =  socket.gethostbyname(socket.gethostname())
print address
print get_netmask("en1")

nm = nmap.PortScanner()
nm.scan(hosts=address, arguments='-n -sP')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    print(host)
