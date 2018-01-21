package designpatterns.creational.factories;

/**
 * Created by eyifang on 2017/11/30.
 */
public class Vegetaria extends Pizza {

    public Vegetaria(){

        this.name ="Vegetaria";
        this.sousage = "Peanut";
        this.sousage = "No Meat";

    }

    @Override
    public void prepare() {
        System.out.println("Preparing Vegetaria");
    }


    @Override
    public void cutting() {
        System.out.println("Cutting Vegetaria");
    }

    @Override
    public void baking() {
        System.out.println("Baking Vegetaria");
    }

    @Override
    public void boxing() {
        System.out.println("Boxing Vegetaria");
    }

    public String toString(){
        return this.name+","+this.dough+","+this.sousage;
    }

}
