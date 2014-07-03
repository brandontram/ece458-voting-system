import pickle
import sys
import socket

GET_CLIENTS = 'getClients'
HOST, PORT = "localhost", 10000

class Serializible:
    """Class to create commands to send to and from server"""
    

    def __init__(self, command):
        self.command = command
        


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