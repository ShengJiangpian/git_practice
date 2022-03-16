"""
@Description : 
@Author      : Su Jingpeng
@Copyright   : 杭州中为光电技术有限公司
@Date        : 2022-03-15 14:49:40
@LastEditors : Su Jingpeng
@LastEditTime: 2022-03-15 16:15:55
@Modified    : 
"""


# import threading
# import time


# exitFlag = 0


# class myTread(threading.Thread):
#     def __init__(self, thread_id, thread_name, delay):
#         threading.Thread.__init__(self)
#         self.thread_id = thread_id
#         self.thread_name = thread_name
#         self.delay = delay

#     def run(self):
#         print("线程开始" + self.thread_name)
#         threadLock.acquire()
#         print_time(self.thread_name, self.delay, 3)
#         threadLock.release()
#         print("线程结束" + self.thread_name)


# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1


# threadLock = threading.Lock()
# threads = []

# thread1 = myTread(1, "Thread-1", 1)
# thread2 = myTread(2, "Thread-2", 2)


# thread1.start()
# thread2.start()

# threads.append(thread1)
# threads.append(thread2)

# for t in threads:
#     t.join()
# print("退出主线程")