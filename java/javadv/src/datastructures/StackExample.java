package datastructures;

import java.util.Stack;

/**
 * Created by eyifang on 2017/11/7.
 */
public class StackExample {

    public static void main(String[] args) {
        Stack  stack = new Stack();

        for(int i=0;i<=10;i++){
            stack.push(i);
        }
        //LILO
        System.out.println(stack);
        stack.pop();
        System.out.println(stack);
        System.out.println(stack.empty());
        System.out.println(stack.peek());

        while(!stack.empty()){
            System.out.print(stack.peek());
            stack.pop();
            System.out.print(",");
        }
        System.out.println("LILO empty!");
    }
}
