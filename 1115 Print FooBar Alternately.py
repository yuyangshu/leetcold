class FooBar:
    def __init__(self, n):
        from threading import Semaphore

        self.n = n
        self._foo = Semaphore(1)
        self._bar = Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self._foo.acquire()
            printFoo()
            self._bar.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self._bar.acquire()
            printBar()
            self._foo.release()
