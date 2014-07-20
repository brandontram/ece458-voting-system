import socket
import SocketServer
import pickle
from OpenSSL import SSL

def make_digest(message):
    return hmac.new(secretKey, message, hashlib.sha1).hexdigest()

class SSLSocketServer(SocketServer.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        SocketServer.BaseServer.__init__(self, server_address, RequestHandlerClass)
        ctx = SSL.Context(SSL.TLSv1_METHOD)
        cert = 'cert.pem'
        ctx.use_privatekey_file(cert)
        ctx.use_certificate_file(cert)
        self.socket = SSL.Connection(ctx, socket.socket(self.address_family,
                                                                self.socket_type))
        if bind_and_activate:
            self.server_bind()
            self.server_activate()

    def shutdown_request(self,request):
        request.shutdown()


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """Handles shizz"""
    def setup(self):
        self.connection = self.request
        self.rfile = socket._fileobject(self.request, "rb", 2048)
        self.wfile = socket._fileobject(self.request, "wb", 2048)

    def handle(self):
        print 'Received request'
        self.data = pickle.load(self.rfile)
        print "Successfully received request from: {}".format(self.client_address[0])

        if self.data.command == 'getClients':
            print "sending clients"
            pickle.dump({'1':'John', '2':'Andrew_ng', '3':'Bill'}, self.wfile, pickle.HIGHEST_PROTOCOL)
            print 'clients sent'
        elif self.data.command == 'postVote':
            print 'vote received: ' + self.data.payload
            pickle.dump("Vote received by server", self.wfile, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    HOST, PORT = "localhost", 10000

    server = SSLSocketServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()