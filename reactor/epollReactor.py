from reactor.impReactor import *

class epollReactor(impReactor):
    def addEvent(self,fd, status, func, arg = None):
        print("xxx")
        pass
    def delEvent(self,fd,status):
        pass
    def loop(self):
        pass