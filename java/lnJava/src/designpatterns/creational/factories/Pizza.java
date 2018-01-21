package designpatterns.creational.factories;

import designpatterns.Print;

import java.util.ArrayList;

/**
 * Created by eyifang on 2017/11/29.
 */
public abstract class Pizza {

    String name ;
    String dough;
    String sousage;
    ArrayList<String> toppings;

    public Pizza(){

    }

    public void prepare(){
        Print.print("I'm preparing");
    };

    public void baking(){
        Print.print("I'm baking");
    };

    public void cutting(){
        Print.print("I'm cutting");
    };

    public void boxing(){
        Print.print("I'm boxing");
    };

    public String toString(){
        StringBuffer sb = new StringBuffer();

        sb.append(name);

        return sb.toString();
    }


}
