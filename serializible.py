import pickle
import sys
import socket

GET_CLIENTS = 'getClients'
HOST, PORT = "localhost", 10000

class Serializible:
    """Class to create commands to send to and from server"""
    

    def __init__(self, command):
        self.command = command
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
        _socket.connect((HOST, PORT))
        ser = Serializible('getClients')
        f = _socket.makefile('wb', 2048)
        pickle.dump(_serializible, f, pickle.HIGHEST_PROTOCOL)

        # Receive data from the server and shut down
        f = _socket.makefile('rb', 2048)
        data = pickle.load(f)
        print 'successfully received pickle: ', data
    except:
        print 'could not send pickle: ', sys.exc_info()[0]
    finally:
        _socket.close()