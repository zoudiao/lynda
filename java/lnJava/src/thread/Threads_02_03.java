package thread;

/**
 * Created by eyifang on 2017/11/2.
 */
public class Threads_02_03 {
    static int counter =1;

    public static void main(String[] args){


     //   Runnable r = ()->{
     //       System.out.println("ID value:"+getID());
     //   };

      //  Thread one = new Thread(r,"one");
     //   one.start();

     //   Thread two = new Thread(r,"two");
     //   two.start();




          /*Example of locking using an object*/
        Runnable r2 = () -> {
            ID id = new ID();
            System.out.println("ID value:"+id.getID());
        };

        Thread three = new Thread(r2,"three");
        three.start();

        Thread four = new Thread(r2,"four");
        four.start();
    }



    public static synchronized int getID(){
        return counter++;
    }
}
