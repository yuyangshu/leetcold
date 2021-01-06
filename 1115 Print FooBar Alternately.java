import java.util.concurrent.Semaphore;

class FooBar {
    private int n;
    private Semaphore fooSem;
    private Semaphore barSem;

    public FooBar(int n) {
        this.n = n;
        this.fooSem = new Semaphore(1);
        this.barSem = new Semaphore(0);
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            this.fooSem.acquire();
            // printFoo.run() outputs "foo". Do not change or remove this line.
            printFoo.run();
            this.barSem.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            this.barSem.acquire();
            // printBar.run() outputs "bar". Do not change or remove this line.
            printBar.run();
            this.fooSem.release();
        }
    }
}
