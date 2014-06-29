import SocketServer
import hashlib
import hmac
import time
from vote import Vote
import database_helpers

secretKey = 'super-secret-key'

def createVote(data):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    vote = Vote(1, 2, now, 3, 4, 5)
    database_helpers.addVoteToDb(vote)

createVote("Stuff")

def make_digest(message):
    return hmac.new(secretKey, message, hashlib.sha1).hexdigest()

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """Handles shizz"""

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data

        message_and_hmac = self.data.split('&')
        message = message_and_hmac[0]
        incoming_digest = message_and_hmac[1]
        expected_digest = make_digest(message)
        print "incoming: " + incoming_digest
        print "expected: " + expected_digest

        if expected_digest != incoming_digest:
            print "DATA CORRUPTED"
        else:
            print "DATA OK"

        self.request.sendall(self.data.upper())

if __name__ == '__main__':
    HOST, PORT = "localhost", 9999

    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()
