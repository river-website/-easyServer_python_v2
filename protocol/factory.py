from protocol.httpProtocol import *


def getProtocol(protocolName):
    if protocolName == 'http':
        return httpProtocol()