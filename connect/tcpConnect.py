from connect.connect import *

class tcpConnect(connect):
    __state = None
    maxPackageSize = 10485760
    __onMessage = None
    __onClosed = None

    def read(self,socket):
        data = self.__state.read(self._socket)
        if data == False:
            self.close()
        elif data != None:
            if self._protocol:
                self._rBuffer += data
                if self.currentPackageSize > 0:
                    if self.currentPackageSize > len(self._rBuffer):
                        return
                else:
                    protocol = self._protocol
                    self.currentPackageSize = protocol.getInfo(self._rBuffer)
                    if self.currentPackageSize == 0:
                        return
                    elif self.currentPackageSize>0 and self.currentPackageSize <= self.maxPackageSize:
                        if self.currentPackageSize > len(self._rBuffer)
                            return
                    else:
                        self.close()
                        return
                buffer = self._protocol.decode(self._rBuffer,self)
            else:
                buffer = data
            if self.__onMessage:
                try:
                    self.__onMessage(self,buffer)
                except Exception as e:
                    pass
    def write(self,socket,data):
        if self._wBuffer:
            len  =self.__state.write(socket,data)
            if len == False:
                self.close()
            elif len == True:
                self._wBuffer = ''
                return True
            else:
                self._wBuffer = len
        #         add event
            return True