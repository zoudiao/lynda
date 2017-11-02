package thread;

/**
 * Created by eyifang on 2017/11/1.
 */
public class TestJoinClass extends Thread {

    public TestJoinClass(String name){
        super(name);
    }

    public void run(){

        for(int i=1;i<=5;i++){
            try{

                Printer.printf(Thread.currentThread());
                Thread.sleep(500);

            }catch (Exception e){
                System.out.println(e);
            }

        }

    }
}
