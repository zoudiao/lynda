package generics;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by eyifang on 2017/10/24.
 */


public class SyntaxExample {

    public static void main(String[] args){

         /*
        * Syntax for a generic method
        * E: Element
        * K,V : Key, Value
        * */

        ArrayList a = new ArrayList();
        a.add(15);
        a.add("15");
        //runtime error , java.lang.String cannot be cast to java.lang.Integer
        // Integer b = (Integer)a.get(1);

        ArrayList<Integer> a1 = new ArrayList<Integer>();
        a1.add(15);
        //compile error
        //a1.add("15");
        //Integer b = a.get(1);

        Pair<Integer, String> p1 = new OrderedPair<>(1,"apple");
        Pair<String, Integer> p2 = new OrderedPair<>("banana",2);
        print(p1.getKey(),p1.getValue());
        print(p2.getKey(),p2.getValue());
        print("Happy","Birthday");


        //type erasure ???
        List<Integer> list1 = new ArrayList<Integer>();
        List rawlist = list1;

        List rawlist2 = new ArrayList();
        List<Integer> list2 = rawlist2;


    }

    //generic method
    public static <K,V> void print(K key, V value){
        System.out.println("key:"+key);
        System.out.println("value:"+value);
    }
}
