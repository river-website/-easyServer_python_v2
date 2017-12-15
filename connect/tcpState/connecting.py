from connect.tcpState.tcpState import *

class connecting(tcpState):
    def read(self,connect):
        socket = connect.getSocket()
        try:
            buffer = socket.recv(65536)
        except Exception as e:
            connect.close()
            return
        if not buffer:
            connect.close()
        return bytes.decode(buffer)
    def write(self,connect,data):
        socket = connect.getSocket()
        data = bytearray(data,'utf-8')
        try:
            len = socket.send(data)
        except Exception as e:
            connect.close()
            return
        if not len:
            connect.close()
            return
        if len < data.__len__():
            buffer = data[len,]
            return buffer
        return True

    def close(self,connect):
        socket = connect.getSocket()
        socket.close()
        connect.setClosed()