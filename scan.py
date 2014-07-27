import sys, argparse, os, nmap, netifaces, socket, threading

parser = argparse.ArgumentParser(description="Detect active man in the middle attacks")

def main():
	args = parser.parse_args()
	gateway = netifaces.gateways()['default']
	if (len(gateway) < 1):
		print("No gateway found")
		sys.exit(2)

	gateway_ip  = gateway[netifaces.AF_INET][0]
	print("Gateway IP:", gateway_ip)
	
	nm = nmap.PortScanner()

	scan_result = nm.scan(hosts = gateway_ip, arguments = '-sP -n')
	true_mac_address = str(scan_result['scan'][gateway_ip]['addresses']['mac'].lower())

	arp_table_raw = os.popen('arp -a')
	for line in arp_table_raw:
		parsed_entry = line.split(' ')
		gateway_ip_string = '(' + gateway_ip + ')'
		if (gateway_ip_string in parsed_entry):
			index = parsed_entry.index(gateway_ip_string)
			arp_mac_address = str(parsed_entry[index + 2]) # mac address is always 2 tokens after IP

	if (true_mac_address == arp_mac_address):
		print(true_mac_address + " == " + arp_mac_address + " (YOU ARE NOT BEING WATCHED)")
	else:
		print(true_mac_address + " != " + arp_mac_address + " (WATCH OUT! YOU ARE BEING WATCHED)")

	threading.Timer(1, main).start()

if __name__ == '__main__':
	main()