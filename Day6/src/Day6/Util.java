package Day6;

import java.util.ArrayList;

public class Util {

    public static ArrayList<Integer> parseData(String data) {
        ArrayList<Integer> parsed = new ArrayList<Integer>();
        for(String field : data.split(" ")) {
            if(!field.isEmpty()) {
                parsed.add(Integer.parseInt(field));
            }
        }
        return parsed;
    }

}
