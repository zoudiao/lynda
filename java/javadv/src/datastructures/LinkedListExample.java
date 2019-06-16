package datastructures;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.ListIterator;

/**
 * Created by eyifang on 2017/11/7.
 */
public class LinkedListExample {

    public static void main(String[] args){

        LinkedList city = new LinkedList();
        city.add("Boston");
        city.add("Miami");
        city.add("Dallas");
        city.add("Atlanta"); // add in the middle
        city.add("New Jersey");
        city.add("Detroit");

        city.addFirst("New York");
        System.out.println(city);
        System.out.println("last city in my list:"+city.getLast());

        ListIterator iterator = city.listIterator(city.size());

        while(iterator.hasPrevious()){// bidirectional
            System.out.println(iterator.previous());
        }


    }
}
