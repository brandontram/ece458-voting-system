import pickle
import sys
import socket, ssl

GET_CLIENTS = 'getClients'
POST_VOTE = 'postVote'
HOST, PORT = "localhost", 10000

class Serializible:
    """Class to create commands to send to and from server"""

    def __init__(self, command, payload=""):
        self.command = command
        self.payload = payload
        self.encrypted = False


    def encryptSelf(self):
        """Encrypts all instance variables"""
        # this function should be more strict, maybe the instance variables should be encrypted during initilization
        # yep, do it that way ^, then wouldnt need to have the encrypted instance variable
        # or maybe it doesnt matter that the data here is not encrypted, think about during a session, all of the data
        # is visible, we just want the transfer of the data from kiosk to server to be secure
        self.encrypted = True
        


def sendSerialized(_socket, _serializible):
    try:
        # Connect to server and send data
        ssl_sock = ssl.wrap_socket(_socket,
                                ca_certs="cert.pem",
                                cert_reqs=ssl.CERT_REQUIRED,
                                ssl_version=ssl.PROTOCOL_TLSv1)
        ssl_sock.connect((HOST, PORT))

        f = ssl_sock.makefile('wb', 2048)
        pickle.dump(_serializible, f, pickle.HIGHEST_PROTOCOL)

        # Receive data from the server and shut down
        f = ssl_sock.makefile('rb', 2048)
        data = pickle.load(f)
        print 'successfully received pickle: ', data
        return data
    except:
        print 'could not send pickle: ', sys.exc_info()[0]
    finally:
        ssl_sock.close()