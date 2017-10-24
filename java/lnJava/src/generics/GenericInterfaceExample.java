package generics;

/**
 * Created by eyifang on 2017/10/24.
 */
public class GenericInterfaceExample {

    public static void main(String[] args){
            GenericList<String> list = new GenericList<>();
            list.add("Good afternoon");

            System.out.println(list.myList);

            //bounded type
            print(new Integer(20));
    }

    public static <T extends Number> void print(T t){
        System.out.println(t);
    }
}
