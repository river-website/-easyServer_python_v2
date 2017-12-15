from connect.tcpState.tcpState import *

class listening(tcpState):
    def read(self,connect):
        socket = connect.getSocket()
        try:
            (clienctSocket, hostPort) = socket.accept()
        except ConnectionError as e:
            connect.close()
            return
        if clienctSocket:
            return (clienctSocket, hostPort)
    def close(self,connect):
        socket = connect.getSocket()
        socket.close()
        connect.setClosed()