import java.math.BigInteger;
import java.util.ArrayList;
import Day6.Race;
import Day6.Util;

public class Main {

    public static void main(String[] args) {
        
        String testInput = """
                Time:      7  15   30
                Distance:  9  40  200""";

        String finalInput = """
                Time:        48     93     84     66
                Distance:   261   1192   1019   1063""";

        String[] splitInput = finalInput.split("\n");

//        PART 1
//        ArrayList<Integer> durations = Util.parseData(splitInput[0]);
//        ArrayList<Integer> records = Util.parseData(splitInput[1]);
//        ArrayList<Race> races = new ArrayList<Race>();
//        for(int count = 0; count < records.size(); count++) {
//            races.add(new Race(durations.get(count), records.get(count)));
//        }

        BigInteger duration = Util.parseData2(splitInput[0]);
        BigInteger record = Util.parseData2(splitInput[1]);
        Race race = new Race(duration, record);

        race.runVariations();
        System.out.println(race.getWaysToWin());

    }
}