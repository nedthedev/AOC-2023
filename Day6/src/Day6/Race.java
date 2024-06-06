package Day6;

public class Race {

    private int record;
    private int duration;
    private int waysToWin;

    public Race(int duration, int record) {
        this.record = record;
        this.duration = duration;
        this.waysToWin = 0;
    }

    public void runVariations() {
        for(int speed = 1; speed < this.duration; speed++) {
            if(speed * (duration-speed) > this.record) {
                this.incrementWaysToWin();
            }
        }
    }

    public void incrementWaysToWin() {
        this.waysToWin++;
    }

    public int getRecord() {
        return this.record;
    }

    public int getTime() {
        return this.duration;
    }

    public int getWaysToWin() {
        return this.waysToWin;
    }

}
