"""
 control.py: Creates queues, starts output and worker threads,
            and pushes inputs into the input queue.
 Modify the control module from the final example of the lesson so that
- instead of asking the user for input
- it generates a random string of alphabetic characters of length one thousand
Similarly modify the output routine to print only the length of the final string.
Test the time it takes the program to run. 
Make sure the workers report when done by printing to console.
"""
from queue import Queue
from output import OutThread
from worker import WorkerThread
from alphaGenerator import alphaGen
from timeit import timeit

WORKERS = 10
inq = Queue(maxsize=int(WORKERS * 1.5))
outq = Queue(maxsize=int(WORKERS * 1.5))
ot = OutThread(WORKERS, outq)
ot.start()
for i in range(WORKERS):
    w = WorkerThread(inq, outq)
    w.start()

instring = alphaGen(1000)
for work in enumerate(instring):
    inq.put(work)
for i in range(WORKERS):
    inq.put(None)
    inq.join()    
# print("Control thread terminating")

# print("ot.start()",timeit("ot.start()"))
# print("lf2 ",timeit("lf2(oldlist)", "from __main__ import lf2, oldlist"))
# print("lf3 ",timeit("lf3(oldlist)", "from __main__ import lf3, oldlist"))
# print("lf4 ",timeit("lf4(oldlist)", "from __main__ import lf4, oldlist"))
