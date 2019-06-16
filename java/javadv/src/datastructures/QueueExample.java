package datastructures;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by eyifang on 2017/11/7.
 */
public class QueueExample {
    public static void main(String[] args) {

        Queue<Integer> queue = new LinkedList();

        for(int i=0;i<=10;i++){
            queue.add(i);
        }

        System.out.println(queue);
        int remove =  queue.remove();
        System.out.println(remove + " is removed");

        System.out.println(queue);

    }
}
