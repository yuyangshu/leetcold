import java.util.concurrent.Semaphore;

class H2O {
    Semaphore hSem, oSem;

    public H2O() {
        this.hSem = new Semaphore(2);
        this.oSem = new Semaphore(0);
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		this.hSem.acquire();
        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        releaseHydrogen.run();
        this.oSem.release();
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        this.oSem.acquire(2);
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
		releaseOxygen.run();
        this.hSem.release(2);
    }
}
