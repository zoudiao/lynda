/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package generics;



import java.util.ArrayList;
import java.util.Date;

/**
 *
 * @author Producer
 */
public class ComparableExample {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //prior to java 5.0
        Comparable c = new Date();
        //runtime error , not compile time
        //System.out.println(c.compareTo("Monday"));
        Comparable<Date> c2 = new Date();
        //compile error
        //System.out.println(c2.compareTo("Monday"));



    }
    
}
