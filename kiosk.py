import socket
import serializible
import pickle

class Kiosk(object):
	"""Kiosk object, verifies user, creates voets, encrypts votes, sends votes (pickled)"""

	def __init__(self):
		# start server?
		# print output, give user options
		# perform tasks, vote etc
		self.candidates = []
		pass
	
	def getCandidates(self):
		"""Populates the list of candidates from the server"""
		self.candidates.append('John')
		self.candidates.append('Sweeney')
		self.candidates.append('Edgar')
		self.candidates.append('Bill')

	# def sendSerializible(serializible):


HOST, PORT = "localhost", 10000

def sendSerialized(_socket, _serializible):
	f = _socket.makefile('wb', 2048)
	pickle.dump(_serializible, f, pickle.HIGHEST_PROTOCOL)
	f.close()

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    ser = serializible.Serializible('getClients')
    sendSerialized(sock, ser)

    # Receive data from the server and shut down
    f = sock.makefile('rb', 2048)
    data = pickle.load(f)
finally:
    sock.close()

# print "Sent:     {}".format(message_and_hmac)
print "Received: {}".format(data[0])

