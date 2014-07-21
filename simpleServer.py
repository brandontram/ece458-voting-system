import socket, os, operator
from SocketServer import BaseServer
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from OpenSSL import SSL
import markup

HOST, PORT = socket.gethostname(), 8000

candidates = {'1':'John', '2':'Andrew Ng', '3':'Bill'}

class SecureHTTPServer(HTTPServer):
    def __init__(self, server_address, HandlerClass):
        print socket.gethostname()
        BaseServer.__init__(self, server_address, HandlerClass)
        ctx = SSL.Context(SSL.TLSv1_METHOD)
        #server.pem's location (containing the server private key and
        #the server certificate).
        fpem = 'cert.pem'
        ctx.use_privatekey_file (fpem)
        ctx.use_certificate_file(fpem)
        self.socket = SSL.Connection(ctx, socket.socket(self.address_family,
                                                        self.socket_type))
        self.server_bind()
        self.server_activate()


class SecureHTTPRequestHandler(SimpleHTTPRequestHandler):
    def setup(self):
        self.connection = self.request
        self.rfile = socket._fileobject(self.request, "rb", self.rbufsize)
        self.wfile = socket._fileobject(self.request, "wb", self.wbufsize)

    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'html')
        self.end_headers()

        page = markup.page()
        page.init(title = "ECE 458 Voting System")
        page.form()

        sortedDict = sorted(candidates.iteritems(), key=operator.itemgetter(0))
        for key, value in sortedDict:
            page.input(type='radio', name='candidate', value='key')
            page.p(value)

        page.form.close()
        page.input(type='submit', value='submit')

        self.wfile.write(bytes(page))

def test(HandlerClass = SecureHTTPRequestHandler,
         ServerClass = SecureHTTPServer):
    server_address = (HOST, PORT)
    httpd = ServerClass(server_address, HandlerClass)
    sa = httpd.socket.getsockname()
    print "Serving HTTPS on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == '__main__':
    test()