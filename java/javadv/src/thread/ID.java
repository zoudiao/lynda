package thread;

/**
 * Created by eyifang on 2017/11/2.
 */
public class ID {

    private static int counter;

    public static synchronized int getID(){
        return counter ++;
    }
}
