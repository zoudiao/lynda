package designpatterns.creational.factories;

/**
 * Created by eyifang on 2017/11/30.
 */
public class PizzaOrder {

    public static void main(String[] args) {
        PizzaFactory factory = new PizzaFactory();

        Pizza peper = factory.orderPizza("Peperoni");

        peper.prepare();

        peper.baking();

        peper.cutting();

        peper.boxing();


        Pizza vege = factory.orderPizza("Vegetaria");

        vege.prepare();

        vege.baking();

        vege.cutting();

        vege.boxing();
    }
}
