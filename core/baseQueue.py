from threading import *

class baseQueue(object):
    # 队列数组
    queue = []
    # 访问队列的锁
    queueLock = None
    # 判断空的锁
    emptyLock = None
    # 初始化,锁，设置为空
    def __init__(self,useLock=False):
        if useLock:
            self.queueLock = Lock()
            self.emptyLock = Lock()
            self.setEmpty()
    # 请求队列锁
    def acquire(self):
        if self.queueLock:
            if self.queueLock.acquire():
                return
    # 释放队列锁
    def release(self):
        if self.queueLock:
            self.queueLock.release()
    # 等待队列不为空
    def waitNotEmpty(self):
        if self.emptyLock:
            self.emptyLock.acquire()
    # 设置队列为空
    def setEmpty(self):
        if self.emptyLock:
            self.emptyLock.acquire()
    # 设置队列不为空
    def setNotEmpty(self):
        if self.emptyLock:
            self.emptyLock.release()
    # 获取队列元素
    def pop(self):
        self.waitNotEmpty()
        self.acquire()
        ret = self.queue.pop()
        if len(self.queue):
            self.setNotEmpty()
        self.release()
        return ret
    # 增加队列元素
    def push(self,item):
        self.acquire()
        if not len(self.queue):
            self.setNotEmpty()
        self.queue.append(item)
        self.release()
