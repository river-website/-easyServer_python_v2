from core.singleton import *
from protocol.httpProtocol import *

class protocol(singleton):
    def decode(self,data,connect = None):
        pass
    def encode(self,data):
        pass
    def getInfo(self,data):
        pass
    def factoryMethod(self,protocolName):
        if protocolName == 'http':
            return httpProtocol()
