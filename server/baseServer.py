from server.server import *
from connect.factory import *
from reactor.factory import *
from reactor.impReactor import *

from functools import reduce
from socket import *


class baseServer(server):
    __fdMap = {}
    def start(self,data=None):
        getReactor().loop()
    def init(self,data=None,server=None):
        def createConnect(addr):
            connectName = addr.split(":")[0]
            addr = addr.split("//")[1]
            connect = getConnect(connectName)
            socket = self.createSocket(addr)
            connect.setSocket(socket)
            connect.setOnMessage(self.onMessage)
            connect.setListening()
            self.addEvent(socket,impReactor.eventRead,connect.read)
            ret[addr] = socket.fileno()
            self.__fdMap[socket.fileno()] = server
        ret = {}
        list(map(createConnect,data))
        return ret
    def createSocket(self,addr):
        host = addr.split(":")[0]
        port = int(addr.split(":")[1])
        s = socket(AF_INET, SOCK_STREAM)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口复用的关键点
        s.setblocking(0)
        s.bind((host, port))
        s.listen()
        return s
    def addEvent(self,fd,status,func,args=None):
        getReactor().addEvent(fd,status,func,args)
    def onMessage(self,connect,data):
        server = self.__fdMap[connect.getSocket().fileno()]
        (clienctSocket,hostPort) = data
        clienctSocket.setblocking(0)
        tcp = getConnect("tcp")
        tcp.setSocket(clienctSocket)
        tcp.setOnMessage(server.onMessage)
        tcp.setProtocol(server.protocol)
        tcp.setConnecting()
        getReactor().addEvent(clienctSocket, impReactor.eventRead, tcp.read)
