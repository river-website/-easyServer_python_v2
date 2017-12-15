from server.server import *
from server.baseServer import *
from protocol.factory import *
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

        self.protocol = getProtocol("http")
        self.__threadPool = threadPool(100)
        ser = baseServer()
        addrFds = ser.init(list(map(lambda addr:'tcp://'+addr, data.keys())),self)
        list(map(toWebPath,data.keys(),data.values()))
    def onMessage(self,connect,request):
        app = self.__connectToWebPath[connect.getSocket().fileno()]
        connect.send(app.doRequest(request))