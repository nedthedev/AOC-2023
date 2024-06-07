package Day6;

import java.math.BigInteger;
import java.util.ArrayList;

public class Util {

    public static ArrayList<Integer> parseData(String data) {
        ArrayList<Integer> parsed = new ArrayList<Integer>();
        data = data.split(": ")[1];
        for(String field : data.split(" ")) {
            if(!field.isEmpty()) {
                parsed.add(Integer.parseInt(field));
            }
        }
        return parsed;
    }

    public static BigInteger parseData2(String data) {
        System.out.println(data);
        data = data.split(": ")[1].trim().replace(" ", "");
        System.out.println(data);
        return new BigInteger(data);
    }

}
