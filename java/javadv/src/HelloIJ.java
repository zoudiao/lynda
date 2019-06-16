import java.util.Scanner;

/**
 * Created by eyifang on 2017/10/18.
 */
public class HelloIJ {

    public static void main(String[] args){

        //primite


    //arrays
        double[] prices = new double[5];

        Scanner in = new Scanner(System.in);

        System.out.println("enter 5 prices:");

        double total=0 ;

        for (int i=0;i<prices.length;i++){
            prices[i] = in.nextDouble();
            total += prices[i];

        }

        System.out.println(total);

    //data conversion



    }
}
