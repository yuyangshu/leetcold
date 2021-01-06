import java.util.Queue;
import java.util.ArrayDeque;

class BoundedBlockingQueue {
    private Queue<Integer> queue;
    private int capacity;

    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;
        this.queue = new ArrayDeque<Integer>(capacity);
    }

    public synchronized void enqueue(int element) throws InterruptedException {
        while (this.queue.size() == this.capacity) {
            wait();
        }

        this.queue.add(element);
        notifyAll();
    }

    public synchronized int dequeue() throws InterruptedException {
        while (this.queue.size() == 0) {
            wait();
        }

        var element = this.queue.remove();
        notifyAll();
        return element;
    }

    public synchronized int size() {
        return this.queue.size();
    }
}
