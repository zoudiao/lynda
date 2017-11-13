package recursion;

import java.util.Scanner;

/**
 * Created by eyifang on 2017/11/13.
 */
public class RecursionExamples {

    public static void main(String[] args) {

        int[] list = {10,20,30,40,50,60};

        reversePrint(list);

        System.out.println();
        System.out.println("Enter a number for factorial numbers:");
        Scanner sc = new Scanner(System.in);
        int f = sc.nextInt();
        System.out.println("Factorial number is :"+factorial(f));

        System.out.println("Enter two numbers");
        int x = sc.nextInt();
        int y = sc.nextInt();
        greateset(x,y);
    }


    private static void reversePrint(int[] numbers){

        if (numbers.length == 0)
            return;

        int[] a = new int[numbers.length-1];

        for(int i=0;i<numbers.length-1;i++) {
            a[i] = numbers[i + 1];
        }

        reversePrint(a);

      System.out.print(numbers[0]+" ");

    }

    private static int factorial(int n){

        if(n==1)
            return 1;

       return n*factorial(n-1);
    }

    private static int greateset(int a , int b){

        int tmp = a;
        if(a<b){
            a = b;
            b = tmp;
        }

        if(b==0)
            return a;

        return greateset(b, (a%b));

    }

}
