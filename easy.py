from server.factory import *
from core.singleton import *

class easy(singleton):
    def start(self,serverData):
        def startOneServer(serverName,data):
            ser = getServer(serverName)
            ser.init(data)
        self.__back()
        list(map(startOneServer, serverData.keys(),serverData.values()))
        getServer().start()
    def __back(self):
        pass
    def monitor(self):
        pass