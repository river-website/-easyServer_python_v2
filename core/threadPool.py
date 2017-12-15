from core.baseQueue import *

class threadPool(object):
    __threads = []
    __events = None
    __maxSize = 0
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.__events = baseQueue(True)
    # 创建线程
    def createThread(self):
        t = Thread(target=self.runThread)
        t.setDaemon(True)
        t.start()
        self.__threads.append(t)
    # 增加事件
    def addEvent(self,func,args=None):
        self.__events.push((func,args))
        if len(self.__threads)<self.maxSize:
            self.createThread()
    # 线程运行
    def runThread(self):
        while True:
            event = self.__events.pop()
            if event and len(event):
                func = event[0]
                args = event[1]
                try:
                    func(args)
                except Exception as e:
                    pass