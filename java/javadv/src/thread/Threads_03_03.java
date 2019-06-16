package thread;

import java.util.concurrent.CountDownLatch;

/**
 * Created by silver on 2017/11/2.
 */
public class Threads_03_03 {

    public static void main(String[] args) throws InterruptedException{
        CountDownLatch start = new CountDownLatch(1);
        CountDownLatch end = new CountDownLatch(4);

        //create and start threads
        for(int i=0;i<5;++i)
            new Thread(new Worker(start,end)).start();

        try{
            System.out.println("main thread doing something");
            Thread.sleep(1000);
            start.countDown();

            System.out.println("main thread doing something else");
            end.await(); // wait for all threads
        }catch (InterruptedException e){
            System.err.println(e);
        }
    }
}
