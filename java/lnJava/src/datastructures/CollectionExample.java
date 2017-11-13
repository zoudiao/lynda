package datastructures;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Created by eyifang on 2017/11/6.
 */
public class CollectionExample {

    public static void main(String[] args){

        List<Integer> list1 = Arrays.asList(1,2,35,65,78,32,14);
        System.out.println("List1 position 65 is:"+Collections.binarySearch(list1,65));


    }

}
