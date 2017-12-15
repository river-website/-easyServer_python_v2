from server.server import *
from protocol.protocol import *
from core.threadPool import *

class webServer(server):
    __connectToWebPath = {}
    protocol = None
    __threadPool = None

    def start(self,data=None):
        pass
    def init(self,data=None,serv=None):
        def toWebPath(addr,webPath):
            fd = addrFds[addr]
            self.__connectToWebPath[fd] = webPath

        self.protocol = protocol.factoryMethod("http")
        self.__threadPool = threadPool(100)
        ser = server.factoryMethod()
        addrFds = ser.init(data.keys(),self)
        list(map(toWebPath),data.keys(),data.values())
    def onMessage(self,connect,data):
        pass