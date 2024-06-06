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
        ArrayList<Integer> durations = Util.parseData(splitInput[0].split(": ")[1]);
        ArrayList<Integer> records = Util.parseData(splitInput[1].split(": ")[1]);
        ArrayList<Race> races = new ArrayList<Race>();
        for(int count = 0; count < records.size(); count++) {
            races.add(new Race(durations.get(count), records.get(count)));
        }

        int answer = 1;
        for(int i = 0; i < races.size(); i++) {
            races.get(i).runVariations();
            answer *= races.get(i).getWaysToWin();
        }

        System.out.println(answer);

    }
}