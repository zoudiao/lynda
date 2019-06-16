package generics;

import java.util.ArrayList;

/**
 * Created by eyifang on 2017/10/24.
 */
public class ChallengeObjective{

    public static void main(String[] args){


        ArrayList<String> list = new ArrayList<>();
        list.add("hello");
        list.add("nice");
        list.add("big");
        foundIt(list,"wow");
        foundIt(list,"echo");
        foundIt(list,"wow");


    }


    public static<E extends Comparable<E>> boolean foundIt(ArrayList<E> list, E elem){
            boolean found = false;
            for(E element:list){
               //not equals
               if(elem.equals(element)){
                   found = true;
                   break;
               }else{
                  // list.add(elem);
               }

               found = false;
            }
            return found;
    }
}
