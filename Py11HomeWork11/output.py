"""
  output.py: The output thread for the miniature framework.
  Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime,
  using a construct called "lambda". This is not exactly the same as lambda in functional programming languages, 
  but it is a very powerful concept that's well integrated into Python and is often used in conjunction with typical
  functional concepts like filter(), map() and reduce(). 
"""
identity = lambda x: x  # List Comprehension
import threading

class OutThread(threading.Thread):
    def __init__(self, N, q, sorting=True, *args, **kw):
        """Initialize thread and save queue reference"""
#        print("Output Class Started")
        threading.Thread.__init__(self, *args, **kw)
        self.queue = q
        self.workers = N
        self.sorting = sorting
        self.output = []
        
    def run(self):
        """Extracts items from the output queue and print untill all are done"""
        while self.workers:
            p = self.queue.get()
            if p is None:
                self.workers -= 1
            else:
                # This is a real output packet
                self.output.append(p)
#        print("string 1","".join(c for i,c in (identity)(self.output)))
        print(len("".join(c for (i, c) in (sorted if self.sorting else identity)(self.output))))

