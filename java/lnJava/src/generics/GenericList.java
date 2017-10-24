package generics;

/**
 * Created by eyifang on 2017/10/24.
 */
public class GenericList<T> implements GenericInterface<T>{

    public T myList;
    public void add(T t){
        myList = t;
    }


}
