package thread;

/**
 * Created by eyifang on 2017/11/2.
 */
public class Countdown {

    public void printCount(){

        try{

            for(int i=10;i>0;i--){

                System.out.println(" --- "+i);
            }

            System.out.println("BlastOff!");
        }catch (Exception e){
            System.out.println("Thread interrupted");
        }
    }

}
