from reactor.impReactor import *
import selectors

class selectReactor(impReactor):
    # epoll
    epoll = None
    # 初始化
    def __init__(self):
        self.initReactor()
    #  初始化reactor
    def initReactor(self):
        _ServerSelector = selectors.SelectSelector
        self.epoll = _ServerSelector()

      # 新增事件
    def addEvent(self,fd,status,func,args=None):
        self.epoll.register(fd,status,(func,args))

    # 删除事件
    def delEvent(self,fd,status):
        self.epoll.unregister(fd)

    # 循环loop
    def loop(self):
        while True:
            ready = self.epoll.select()
            for selectorKey,status in ready:
                func = selectorKey.data[0]
                args = selectorKey.data[1]
                func(selectorKey.fileobj,args)