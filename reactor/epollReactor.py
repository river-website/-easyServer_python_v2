from reactor.reactor import *

class epollReactor(reactor):
    def addEvent(self,fd, status, func, arg = None):
        pass
    def delEvent(self,fd,status):
        pass
    def loop(self):
        pass