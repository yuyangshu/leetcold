class FizzBuzz {
    private int n, current;

    public FizzBuzz(int n) {
        this.n = n;
        this.current = 1;
    }

    // printFizz.run() outputs "fizz".
    public synchronized void fizz(Runnable printFizz) throws InterruptedException {
        while (this.current <= this.n) {
            if (this.current % 3 == 0 && this.current % 5 != 0) {
                printFizz.run();
                this.current += 1;
                notifyAll();
            }
            else {
                wait();
            }
        }
    }

    // printBuzz.run() outputs "buzz".
    public synchronized void buzz(Runnable printBuzz) throws InterruptedException {
        while (this.current <= this.n) {
            if (this.current % 3 != 0 && this.current % 5 == 0) {
                printBuzz.run();
                this.current += 1;
                notifyAll();
            }
            else {
                wait();
            }
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public synchronized void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while (this.current <= this.n) {
            if (this.current % 3 == 0 && this.current % 5 == 0) {
                printFizzBuzz.run();
                this.current += 1;
                notifyAll();
            }
            else {
                wait();
            }
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public synchronized void number(IntConsumer printNumber) throws InterruptedException {
        while (this.current <= this.n) {
            if (this.current % 3 != 0 && this.current % 5 != 0) {
                printNumber.accept(this.current);
                this.current += 1;
                notifyAll();
            }
            else {
                wait();
            }
        }
    }
}
