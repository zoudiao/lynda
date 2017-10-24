package generics;

import java.util.ArrayList;

/**
 * Created by eyifang on 2017/10/24.
 */
public class EliminateDuplicates {

    public static void main(String[] args){

        ArrayList<String> list = new ArrayList<>();
        list.add("red");
        list.add("green");
        list.add("blue");
        list.add("green");
        list.add("yellow");
        list.add("orange");
        list.add("blue");
        ArrayList<String> list2 = removeDups(list);

        System.out.println(list2);
    }

    public static <E extends Comparable<E>>ArrayList<E> removeDups(ArrayList<E> list){
        boolean found = false;

        if(list.size()==0)
            return list;

        ArrayList<E> newList = new ArrayList<>();
        newList.add(list.get(0));

        for(int i=1; i<list.size();i++){
            for(int j=0;j<newList.size();j++){
                if(list.get(i).compareTo(newList.get(j))==0){
                    found = true;
                    break;
                }
            }

            if(found==false){
                newList.add(list.get(i));
            }
            found = false;
        }

        return newList;
    }
}
