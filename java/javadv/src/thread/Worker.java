package thread;

import java.util.concurrent.CountDownLatch;

/**
 * Created by silver on 2017/11/2.
 */
public class Worker extends Thread {

    private final CountDownLatch start;
    private final CountDownLatch end;

   public  Worker(CountDownLatch start, CountDownLatch end){
        this.start = start;
        this.end = end;

    }

    public void run(){
        try
        {

            printInfo("thread entered run()");
            start.await(); //wait before proceeding
            printInfo("doing work");
            Thread.sleep(3000);
            end.countDown(); //reduce count
        }catch (InterruptedException e){
            System.err.println(e);
        }
    }

    void printInfo(String s){
        System.out.println(System.currentTimeMillis()+":"+Thread.currentThread()+":"+s);
    }
}
