package designpatterns.creational.factories;

/**
 * Created by eyifang on 2017/11/30.
 */
public class Peperoni extends Pizza {

    public Peperoni(){
        this.name ="Peperoni";
        this.sousage = "Peper";
        this.sousage = "Pork";
    }

    @Override
    public void prepare() {
        System.out.println("Preparing Peperoni");
    }


    @Override
    public void cutting() {
        System.out.println("Cutting Peperoni");
    }

    @Override
    public void baking() {
        System.out.println("Baking Peperoni");
    }

    @Override
    public void boxing() {
        System.out.println("Boxing Peperoni");
    }


    public String toString(){
        return this.name+","+this.dough+","+this.sousage;
    }

}
