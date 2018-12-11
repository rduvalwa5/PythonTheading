'''
Created on Dec 9, 2018

@author: rduvalwa2
'''
"""
 thread.py: Use threading.Lock to ensure threads run sequentially.
"""
import threading
import time
class MyThread(threading.Thread):
    def __init__(self, lock, *args, **kw):
        threading.Thread.__init__(self, *args, **kw)
#        self.sleeptime = sleeptime
        self.lock = lock
    def run(self):
        for i in range(10):
#            for j in range(500000):
#                k = j*j
           self.lock.acquire()
           time.sleep(0.1)
           self.lock.release()
#            print(self.name, "finished pass", i)
        print(self.name, "finished")
#        print(self.name, "finished after", self.sleeptime, "seconds")
lock = threading.Lock()
bgthreads = threading.active_count()
tt = [MyThread(lock) for i in range(6)]
for t in tt:
    print(t)
    t.start()
print("Threads started")
while threading.active_count() > bgthreads:
    time.sleep(2)
    print("tick")