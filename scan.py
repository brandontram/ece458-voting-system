
import sys
import nmap, netifaces, socket


# def procc():
# 	iface = "en0"
# 	address =  socket.gethostbyname(socket.gethostname())


# 	nm = nmap.PortScanner()
# 	nm.scan(hosts=address, arguments='-n -sO')
# 	hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
# 	for host, status in hosts_list:
	    # print(host)


def main():
	
	if (len(sys.argv) == 2):
		iface = sys.argv[2]

	gateway = netifaces.gateways()
	gateway_ip  = gateway['default'][netifaces.AF_INET][0]

	print("Gateway IP:", gateway_ip)
	
	nm = nmap.PortScanner()

	scan_result = nm.scan(hosts=gateway_ip, arguments='-sO -n')
	mac_address = scan_result['scan'][gateway_ip]['addresses']['mac']

	print('mac address', mac_address)


if __name__ == '__main__':
	main()