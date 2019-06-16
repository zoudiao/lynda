package thread;

/**
 * Created by silver on 2017/10/31.
 */
public class Threads_01_03  {

    public static void main(String[] args) throws InterruptedException {

        //print information about the current thread
        Printer.printf(Thread.currentThread());

        //Create a runnable object that prints information about the thread
        Runnable r1 = () -> {
                Thread thd = Thread.currentThread();
                Printer.printf(thd);
        };

        //Create thread t1 and print the information REFORCE calling start()
        Thread t1 = new Thread();
        Printer.printf(t1);
            t1.start();
        Printer.printf(t1);

        //Create thread t2 with only a runnable object and no name
        Thread t2 = new Thread(r1);
        t2.start();

        //put main thread to sleep for 2 seconds
        Thread.sleep(2000);

        //change the name of thread 2 and print out its info
        t2.setName("Thread t2");
        Printer.printf(t2);

        //print info about current thread
        Printer.printf(Thread.currentThread());
    }

}
