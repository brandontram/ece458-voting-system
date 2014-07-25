import sys, os, nmap, netifaces, socket

def main():
	gateway = netifaces.gateways()
	gateway_ip  = gateway['default'][netifaces.AF_INET][0]
	print("Gateway IP:", gateway_ip)
	
	nm = nmap.PortScanner()

	scan_result = nm.scan(hosts = gateway_ip, arguments = '-sO -n')
	true_mac_address = str(scan_result['scan'][gateway_ip]['addresses']['mac'].lower())

	print('true mac address', true_mac_address)

	arp_table_raw = os.popen('arp -a')
	for line in arp_table_raw:
		parsed_entry = line.split(' ')
		gateway_ip_string = '(' + gateway_ip + ')'
		if (gateway_ip_string in parsed_entry):
			print(parsed_entry)
			index = parsed_entry.index(gateway_ip_string)
			arp_mac_address = str(parsed_entry[index + 2]) # mac address is always 2 tokens after IP
			print('arp mac address:' + arp_mac_address)

	# ARP returns mac addresses without last 0
	if (len(arp_mac_address) < len(true_mac_address)):
		arp_mac_address += '0'

	if (true_mac_address == arp_mac_address):
		print(true_mac_address + " == " + arp_mac_address + " (YOU ARE NOT BEING WATCHED)")
	else:
		print(true_mac_address + " != " + arp_mac_address + " (WATCH OUT! YOU ARE BEING WATCHED)")


if __name__ == '__main__':
	main()