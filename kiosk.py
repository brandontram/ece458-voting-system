import socket
import serializible
import pickle
import operator

class Kiosk(object):
	"""Kiosk object, verifies user, creates votes, encrypts votes, sends votes (pickled)"""

	def __init__(self):
		# start server?
		# print output, give user options
		# perform tasks, vote etc
		self.candidates = {}
		self.userlogin()
		self.getCandidates()

		sortedDict = sorted(self.candidates.iteritems(), key=operator.itemgetter(0))
		for key, value in sortedDict:
			print "Enter " + key + " to vote for " + value

		votedFor = raw_input()
		print "You voted for " + self.candidates[votedFor] + " (Candidate " + votedFor + ")"

		self.sendVote(votedFor)

	def getCandidates(self):
		"""Populates the list of candidates from the server"""
		_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		req     = serializible.Serializible(serializible.GET_CLIENTS)
		self.candidates = serializible.sendSerialized(_socket, req)

	def userlogin(self):
		pass

	def receiveVote(self):
		pass

	def sendVote(self, votedFor):
		_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		req     = serializible.Serializible(serializible.POST_VOTE, votedFor)
		serializible.sendSerialized(_socket, req)

if __name__ == '__main__':
	k = Kiosk()