package thread;

/**
 * Created by eyifang on 2017/11/2.
 */
public class Threads_02_02 {
    static int counter =1;

    public static void main(String[] args){
        Runnable r = ()->{
            System.out.println("ID value:"+getID());
        };

        Thread one = new Thread(r,"one");
        one.start();

        Thread two = new Thread(r,"two");
        two.start();
    }


    public static int getID(){
        return counter++;
    }
}
