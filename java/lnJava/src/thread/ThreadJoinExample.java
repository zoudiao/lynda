package thread;

/**
 * Created by eyifang on 2017/11/1.
 */
public class ThreadJoinExample {


    public static void main(String[] args){
        TestJoinClass t1 = new TestJoinClass("t1");
        TestJoinClass t2 = new TestJoinClass("t2");
        TestJoinClass t3 = new TestJoinClass("t3");

        t1.start();
        t2.start();

        try{
            t2.join();
        }catch (Exception e){
            System.out.println(e);
        }



        //thread 3 won't start until thread 2 is completed
        t3.start();
    }
}
