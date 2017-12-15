from core.singleton import *
from server.webServer import *
from server.baseServer import *

class server(singleton):
    def start(self,data=None):
        pass
    def init(self,data=None,server=None):
        pass
    def onMessage(self,connect,data):
        pass
    def factoryMethod(self,serverName=None):
        if serverName == 'webServer':
            return webServer()
        else:
            return baseServer()