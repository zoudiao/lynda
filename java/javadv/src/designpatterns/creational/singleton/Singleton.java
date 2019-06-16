package designpatterns.creational.singleton;

/**
 * Created by eyifang on 2017/12/1.
 */
public class Singleton {

    public  static Singleton instance = null;


    public static Singleton  getInstance(){

        if(instance == null){
            instance = new Singleton();
        }

        return instance;

    }

    public void print(){
        System.out.println("I'm a signleton");
    }
}
