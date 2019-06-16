package datastructures;

import java.util.ArrayList;
import java.util.Iterator;

/**
 * Created by eyifang on 2017/11/7.
 */
public class ArrayListExample {
    public static void main(String[] args){

        String[] platform1 = {"PS4"};
        String[] platform2 = {"Wii","Box"};
        String[] platform3 = {"IOS","Android"};

        VideoGame game1 = new VideoGame("poker game",1980,"good",platform1);
        VideoGame game2 = new VideoGame("honor",2016,"great",platform3);
        VideoGame game3 = new VideoGame("crazy bird", 2008,"good",platform2);

        ArrayList<VideoGame> games = new ArrayList<>();

        games.add(game1);
        games.add(game2);
        print(games);
        games.add(0,game3);
        print(games);

    }

    public static void print(ArrayList<VideoGame> games){

        Iterator iterator = games.iterator();

        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }


    }
}
