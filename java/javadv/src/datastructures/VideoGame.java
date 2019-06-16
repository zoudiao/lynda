package datastructures;

import java.util.ArrayList;

/**
 * Created by eyifang on 2017/11/7.
 */
public class VideoGame {

    private String title;
    private Integer year;
    private String rating;
    private String[] platforms;

    public VideoGame(String title, Integer year, String rating, String[] platforms){
        this.title = title;
        this. year = year;
        this.rating = rating;
        this.platforms = platforms;
    }


    public String getPlatforms(){
        String result = "";
        for (int i =0;i<platforms.length;i++){
            result += platforms[i]+"|";
        }

        return result;
    }
    public String toString(){
        return "Title:"+title+",Year:"+year+",Rating:"+rating+",Platforms:"+getPlatforms();
    }
}
