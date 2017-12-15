from connect.connect import *
from connect.tcpState.connecting import *
from connect.tcpState.closed import *
from connect.tcpState.listening import *
from reactor.factory import *
from reactor.impReactor import *

class tcpConnect(connect):
    __state = None
    maxPackageSize = 10485760
    __onMessage = None
    __onClosed = None

    def read(self,socket,args=None):
        data = self.__state.read(self)
        if data:
            if self._protocol:
                self._rBuffer += data
                if self._currentPackageSize > 0:
                    if self._currentPackageSize > len(self._rBuffer):
                        return
                else:
                    protocol = self._protocol
                    self._currentPackageSize = protocol.getInfo(self,self._rBuffer)
                    if self._currentPackageSize == 0:
                        return
                    elif self._currentPackageSize>0 and self._currentPackageSize <= self.maxPackageSize:
                        if self._currentPackageSize > len(self._rBuffer):
                            return
                    else:
                        self.close()
                        return
                buffer = self._protocol.decode(self._rBuffer)
            else:
                buffer = data
            if self.__onMessage:
                try:
                    self.__onMessage(self,buffer)
                except Exception as e:
                    pass

    def write(self,socket,data):
        if self._wBuffer:
            len  =self.__state.write(self,self._wBuffer)
            if len == False:
                self.close()
            elif len == True:
                self._wBuffer = ''
                return True
            else:
                self._wBuffer = len
            return True

    def send(self, data):
        self._wBuffer += data
        if self._protocol:
            self._wBuffer = self._protocol.encode(self._wBuffer)
        getReactor().delEvent(self._socket, impReactor.eventRead)
        getReactor().addEvent(self._socket, impReactor.eventWrite,self.write)

    def close(self):
        self.__state.closed(self)
        getReactor().delEvent(self._socket, impReactor.eventRead)
        getReactor().delEvent(self._socket, impReactor.eventWrite)

    def setOnMessage(self,func):
        self.__onMessage = func
    
    def setOnClosed(self,func):
        self.__onClosed = func
    

    def setListening(self):
        self.__state = listening()
    
    def setConnecting(self):
        self.__state = connecting()
    
    def setClosed(self):
        self.__state = closed()
    