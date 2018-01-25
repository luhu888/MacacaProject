# -*- coding: utf-8 -*-
# __author__=luhu
import queue
import threading
import time

exitFlag = 0

'''
    threading.currentThread(): 返回当前的线程变量。
    threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
    除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
        run(): 用以表示线程活动的方法。
        start():启动线程活动。
        join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
        isAlive(): 返回线程是否活动的。
        getName(): 返回线程名。
        setName(): 设置线程名。
        '''


class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)

    """
    Queue.qsize() 返回队列的大小
    Queue.empty() 如果队列为空，返回True,反之False
    Queue.full() 如果队列满了，返回True,反之False
    Queue.full 与 maxsize 大小对应
    Queue.get([block[, timeout]])获取队列，timeout等待时间
    Queue.get_nowait() 相当Queue.get(False)
    Queue.put(item) 写入队列，timeout等待时间
    Queue.put_nowait(item) 相当Queue.put(item, False)
    Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
    Queue.join() 实际上意味着等到队列为空，再执行别的操作
    """


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print(time.ctime(time.time())+"%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
