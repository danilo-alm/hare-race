import threading


class Semaphore:
    def __init__(self, initial):
        self.value = initial
        self.lock = threading.Lock()

    def acquire(self):
        with self.lock:
            if self.value > 0:
                self.value -= 1
                return

    def release(self):
        with self.lock:
            self.value += 1
