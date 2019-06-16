package generics;

/**
 * Created by eyifang on 2017/10/24.
 */
public class Person<E> {

    public E e;

    public void setPerson(E e){
        this.e = e;

    }

    public E getPerson(){
        return e;
    }
}
