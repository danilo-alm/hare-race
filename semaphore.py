import threading


class Semaphore:
    def __init__(self, value=1):
        if value < 0:
            raise ValueError("Semaphore initial value must be >= 0")
        self._value = value
        self._value_lock = threading.Lock()
        self._nonzero = threading.Condition(self._value_lock)

    def acquire(self):
        with self._nonzero:
            while self._value == 0:
                self._nonzero.wait()
            self._value -= 1

    def release(self):
        with self._nonzero:
            self._value += 1
            self._nonzero.notify()
