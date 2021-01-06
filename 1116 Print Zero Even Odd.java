import java.util.concurrent.Semaphore;

class ZeroEvenOdd {
    private int n;
    private Semaphore zeroSem, oddSem, evenSem;

    public ZeroEvenOdd(int n) {
        this.n = n;
        this.zeroSem = new Semaphore(1);
        this.oddSem = new Semaphore(0);
        this.evenSem = new Semaphore(0);
            }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        var nextIsOdd = true;

        for (var i = 0; i < this.n; i ++) {
            this.zeroSem.acquire();
            printNumber.accept(0);

            if (nextIsOdd) {
                oddSem.release();
            }
            else {
                evenSem.release();
            }

            nextIsOdd = !nextIsOdd;
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (var i = 2; i <= this.n; i += 2) {
            this.evenSem.acquire();
            printNumber.accept(i);
            this.zeroSem.release();
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (var i = 1; i <= this.n; i += 2) {
            this.oddSem.acquire();
            printNumber.accept(i);
            this.zeroSem.release();
        }
    }
}
