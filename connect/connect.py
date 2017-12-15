class connect:
    _socket = None
    _protocol = None
    _remoteAddress = ''
    _rBuffer = ''
    _wBuffer = ''
    _currentPackageSize = 0
    def read(self,socket,args=None):
        pass
    def write(self,socket,data):
        pass
    def send(self,data):
        pass
    def close(self):
        pass

    def getSocket(self):
        return self._socket
    def setSocket(self,socket):
        self._socket = socket
    def getRemoteAddress(self):
        return self._remoteAddress
    def setRemoteAddress(self,remoteAddress):
        self._remoteAddress = remoteAddress
    def getProtocol(self):
        return self._protocol
    def setProtocol(self,protocol):
        self._protocol = protocol
    def getRemoteIp(self):
        pass
        # pos = strrpos(self._remoteAddress, ':')
        # return ($pos)?trim(substr(self._remoteAddress, 0, $pos), '[]'):''
    def getRemotePort(self):
        pass
        # return (self._remoteAddress)? (int)substr(strrchr(self._remoteAddress, ':'), 1):0

