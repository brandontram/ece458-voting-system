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
		self.userlogin()
		self.getCandidates()
		# show candidates to user
	
	def getCandidates(self):
		"""Populates the list of candidates from the server"""
		_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		req     = serializible.Serializible(serializible.GET_CLIENTS)
		serializible.sendSerialized(_socket, req)

	def userlogin(self):
		pass

	def receiveVote(self):
		pass

if __name__ == '__main__':
	k = Kiosk()