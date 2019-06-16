package datastructures;


import java.util.Arrays;

import java.util.Iterator;
import java.util.List;

/**
 * Created by eyifang on 2017/11/7.
 */
public class IteratorExample {

    public  static void main(String[] args){

        List<String> list = Arrays.asList("orange","red","blue","white","black");
        Iterator iterator = list.iterator();
        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }


    }
}
