from core.singleton import *
from threading import *
from core.baseQueue import *
class impReactor(singleton):
    eventTime 		= 1
    eventRead 		= (1 << 0)
    eventWrite 		= (1 << 1)
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
