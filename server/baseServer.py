from server.server import *


class baseServer(server):
    def start(self,data=None):
        pass
    def init(self,data=None,server=None):
        pass
    def onMessage(self,connect,data):
        pass
        # 创建server socket
    def createServerSocket(self, data):
        host = data[0]
        port = data[1]
        s = socket(AF_INET, SOCK_STREAM)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口复用的关键点
        s.setblocking(0)
        s.bind((host, port))
        s.listen()
        return (s, (host, port))