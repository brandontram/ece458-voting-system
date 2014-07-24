import socket, os, operator
from SocketServer import BaseServer
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from OpenSSL import SSL
import markup

HOST, PORT = socket.gethostname(), 8000

candidates = {'1':'John', '2':'Andrew Ng', '3':'Bill'}
radioBtnFieldName = 'candidate'

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

    def shutdown_request(self,request):
        request.shutdown()


class SecureHTTPRequestHandler(SimpleHTTPRequestHandler):
    def setup(self):
        self.connection = self.request
        self.rfile = socket._fileobject(self.request, "rb", self.rbufsize)
        self.wfile = socket._fileobject(self.request, "wb", self.wbufsize)

    def do_GET(self):
        page = markup.page()
        page.init(title = "ECE 458 Voting System")
        page.form(method = "POST")

        sortedDict = sorted(candidates.iteritems(), key=operator.itemgetter(0))
        for key, value in sortedDict:
            if (key == '1'):
                page.input(type='radio', name=radioBtnFieldName, value=key, checked=True)
            else:
                page.input(type='radio', name='candidate', value=key)
            page.p(value)

        page.input(type='submit', value='submit')
        page.form.close()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(str(page)))
        self.end_headers()

        self.wfile.write(page)

    def do_POST(self):
        postBodyLen = int(self.headers.getheader('content-length', 0))
        postBody = self.rfile.read(postBodyLen)
        print postBody

        votedId = postBody[len(radioBtnFieldName) + 1:]

        page = markup.page()
        page.init(title = "Thanks for voting!")
        page.p("You voted for candidate " + votedId + ", " + candidates[votedId])
        page.button(type='button', onclick="history.go(-1);return true;")
        page.p("Vote Again")
        page.button.close()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(str(page)))
        self.end_headers()
        self.wfile.write(page)

def test(HandlerClass = SecureHTTPRequestHandler,
         ServerClass = SecureHTTPServer):
    server_address = (HOST, PORT)
    httpd = ServerClass(server_address, HandlerClass)
    sa = httpd.socket.getsockname()
    print "Serving HTTPS on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == '__main__':
    test()