from core.singleton import *
from server.server import *

class easy(singleton):
    def start(self,serverData):
        def startOneServer(serverName,data):
            ser = server.factoryMethod(serverName)
            ser.init(data)
        self.__back()
        list(map(startOneServer, serverData.keys(),serverData.values()))
        server.factoryMethod().start()
    def __back(self):
        pass
    def monitor(self):
        pass