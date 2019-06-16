package thread;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;


/**
 * Created by silver on 2017/11/2.
 */
public class Threads_03_02 {


    public static void main(String[] args){
        ExecutorService executor = Executors.newFixedThreadPool(5);

        for(int i=0;i<10;i++){
            Runnable worker = new WorkerThread("I'm thread"+i);

            executor.execute(worker);
        }

        executor.shutdown();

        while (!executor.isTerminated()){

        }

        System.out.println("Finished all threads");
    }
}
