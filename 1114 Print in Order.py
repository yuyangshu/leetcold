class Foo:
    def __init__(self):
        from threading import Semaphore
        self._first = Semaphore(0)
        self._second = Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self._first.release()
        

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self._first.acquire()
        printSecond()
        self._second.release()
        self._first.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self._second.acquire()
        printThird()
        self._second.release()
