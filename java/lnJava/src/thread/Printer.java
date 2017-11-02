package thread;

/**
 * Created by eyifang on 2017/11/1.
 */
public  class Printer {

    public static void printf(Thread td){

        System.out.printf("%s is %salive and in %s " +"state%n and priority %d \n",td.getName(),
                td.isAlive() ? "": "not ",
                td.getState(),
                td.getPriority());

    }
}
