from core.singleton import *
from reactor.epollReactor import *
from reactor.selectReactor import *

class reactor(singleton):
    eventTime 		= 1
    eventRead 		= 2
    eventWrite 		= 4
    eventSignal	    = 8
    eventTimeOnce   = 16
    eventClock		= 32
    eventExcept 	= 64

    _allEvent = []
    def addEvent(self,fd, status, func, arg = None):
        pass
    def delEvent(self,fd,status):
        pass
    def loop(self):
        pass
    def factoryMethod(self):
        a = 1
        if a:
            return epollReactor()
        else:
            return selectReactor()