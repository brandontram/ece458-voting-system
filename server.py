import socket
import SocketServer
import serializible
import pickle

def make_digest(message):
    return hmac.new(secretKey, message, hashlib.sha1).hexdigest()

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """Handles shizz"""

    def handle(self):
        f = self.request.makefile('rb', 2048)
        self.data = pickle.load(f)
        print "Successfully received request from: {}".format(self.client_address[0])

        if self.data.command == 'getClients':
            print "sending clients"
            f = self.request.makefile('wb', 2048)
            pickle.dump(['John', 'Andrew_ng', 'Bill'], f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    HOST, PORT = "localhost", 10000

    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()