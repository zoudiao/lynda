package thread;

/**
 * Created by eyifang on 2017/11/2.
 */
public class CountdownMain {


    public static void main(String[] args){

        Countdown CD = new Countdown();

        Runnable r = () -> {

           // synchronized (CD){
                CD.printCount();
          //  }

        };


        Thread one = new Thread(r,"one");
        Thread two = new Thread(r, "two");
        one.start();
        two.start();
    }
}
//--- 10
//--- 9
//--- 8
//--- 7
//--- 6
//--- 5
//--- 4
//--- 3
//--- 2
//--- 1
//BlastOff!
//--- 10
//--- 9
//--- 8
//--- 7
//--- 6
//--- 5
//--- 4
//--- 3
//--- 2
//--- 1
//BlastOff!
