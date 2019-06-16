package designpatterns.creational.singleton;

/**
 * Created by eyifang on 2017/12/1.
 */
public class SingletonDemo {

    public static void main(String[] args) {

        Singleton instance = Singleton.getInstance();

        instance.print();

    }
}
