package datastructures;

import java.util.ArrayList;
import java.util.LinkedList;

/**
 * Created by eyifang on 2017/11/7.
 * Create an ArrayList of grocery items
 * Create a second list of more items
 * Add the extra items to your original list
 * Search for and remove an item
 *
 */
public class GroceryList {


    public static void main(String[] args) {


        ArrayList<String> grocery = new ArrayList<>();
        grocery.add("sheet");
        grocery.add("paper");
        grocery.add("bag");
        grocery.add("dessert");

        ArrayList<String> grocery2 = new ArrayList<>();
        grocery2.add("cake");
        grocery2.add("fat");
        grocery2.add("cage");

        grocery.addAll(grocery2);

        System.out.println(grocery);
        for(String g:grocery){
            if (grocery.contains("cage")){
                grocery.remove(g);
                break;
            }
        }
        System.out.println(grocery);



    }

}
