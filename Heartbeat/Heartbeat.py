import threading
from threading import Thread
from time import sleep

__author__ = 'john_carrell'

lock = threading.Lock()

class Heartbeat(Thread):

    def __init__(self, idx, delay=1):
        threading.Thread.__init__(self)
        if idx is None:
            raise ValueError("Must provide a value for 'idx' upon Heartbeat instantiation.")

        self._idx = idx
        self._delay = delay
        self._running = True

    def run(self):
        while self._running:
            lock.acquire()
            print "THUMP THUMP : {}{}".format(" " * (self._idx * 3), self._idx)
            lock.release()
            # threading._sleep(self._delay)
            sleep(self._delay)

    def stop(self):
        print "Killing thread: {}".format(self._idx)
        self._running = False
