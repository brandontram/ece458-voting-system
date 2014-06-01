import socket
import sys
import hmac
import hashlib

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
secretKey = 'super-secret-key'

def make_digest(message):
    return hmac.new(secretKey, message, hashlib.sha1).hexdigest()

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    message_and_hmac = data + '&' + make_digest(data) +"\n"
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(message_and_hmac)

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print "Sent:     {}".format(message_and_hmac)
print "Received: {}".format(received)
