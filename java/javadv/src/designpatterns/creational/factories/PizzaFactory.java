package designpatterns.creational.factories;

/**
 * Created by eyifang on 2017/11/30.
 */
public class PizzaFactory {

    Pizza pizza;

    public Pizza orderPizza(String name){


        if (name.equals("Peperoni")){
            pizza =  new Peperoni();
        }else if(name.equals("Vegetaria")){
            pizza = new Vegetaria();
        }

        return pizza;

    }
}
