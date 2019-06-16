package thread;

/**
 * Created by silver on 2017/11/2.
 */
public class WorkerThread implements Runnable{

    private final String message;

    public WorkerThread(String message){
        this.message = message;
    }


    public void run(){
        System.out.println(Thread.currentThread().getName()+" (Start) message =" +message);

        //call workToBeDone method to simulate a delay
        workToBeDone();

        System.out.println(Thread.currentThread().getName()+" (End)");
    }


    private void workToBeDone(){
        try{
            Thread.sleep(2000);
        }catch (InterruptedException e)
        {
            e.printStackTrace();
        }
    }

}
