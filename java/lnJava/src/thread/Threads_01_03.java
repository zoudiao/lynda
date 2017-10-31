package thread;

/**
 * Created by silver on 2017/10/31.
 */
public class Threads_01_03  {

    public static void main(String[] args){

        //print information about the current thread
        System.out.printf("%s is %salive and in %s " +"state%n and priority %d \n",Thread.currentThread().getName(),
                Thread.currentThread().isAlive() ? "": "not ",
                Thread.currentThread().getState(),
                Thread.currentThread().getPriority());

        //Create a runnable object that prints information about the thread
        Runnable r1 = () -> {
                Thread thd = Thread.currentThread();
                System.out.printf("%s is %salive and in %s " +"state%n and priority %d \n",thd.currentThread().getName(),
                        thd.currentThread().isAlive() ? "": "not ",
                        thd.currentThread().getState(),
                        thd.currentThread().getPriority());
        };

        //Create thread t1 and print the information REFORCE calling start()
        Thread t1 = new Thread();
        System.out.printf("%s is %salive and in %s " +"state%n and priority %d \n",t1.currentThread().getName(),
                t1.currentThread().isAlive() ? "": "not ",
                t1.currentThread().getState(),
                t1.currentThread().getPriority());


    }

}
