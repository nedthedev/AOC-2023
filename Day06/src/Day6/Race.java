package Day6;

import java.math.BigInteger;

public class Race {

    private BigInteger record;
    private BigInteger duration;
    private int waysToWin;

    public Race(BigInteger duration, BigInteger record) {
        this.record = record;
        this.duration = duration;
        this.waysToWin = 0;
    }

    public void runVariations() {
        for (BigInteger speed = BigInteger.valueOf(0); speed.compareTo(this.duration) <= 0;
             speed = speed.add(BigInteger.ONE)) {
            if(speed.multiply(this.duration.subtract(speed)).compareTo(this.record) > 0) {
                this.incrementWaysToWin();
            }
        }
    }

    public void incrementWaysToWin() {
        this.waysToWin++;
    }

    public BigInteger getRecord() {
        return this.record;
    }

    public BigInteger getTime() {
        return this.duration;
    }

    public int getWaysToWin() {
        return this.waysToWin;
    }

}
