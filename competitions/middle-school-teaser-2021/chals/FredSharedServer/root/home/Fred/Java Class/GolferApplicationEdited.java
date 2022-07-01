// Alex Kalomiris @ RIT, 30th December 2020

class Scratch {
    public static void main(String[] args) {
        Golfer a = new Golfer();
        Golfer b = new Golfer("Palmer, Arnold", 2);
        Golfer c = new Golfer("Crenshaw", "Ben", 1);
        Golfer d = new Golfer(c);

        System.out.println(a.toString());
        //"Tiger Woods has a handicap of 0."
        System.out.println(b.getHandicap());
        //"2"
        b.setHandicap(4);
        System.out.println(b.getHandicap());
        //"4"
        System.out.println(a.compareTo(b));
        //Compares the handicap of the golfers
    }
}

class Golfer {

    private String fn;
    private String ln;
    private int handicap;

    Golfer() {
        this.fn = "Tiger";
        this.ln = "Woods";
        this.handicap = 0;
    }

    Golfer(Golfer g){
        this.fn = g.getFn();
        this.ln = g.getLn();
        this.handicap = g.getHandicap();
    }

    Golfer(String full, int h){
        String[] splits = full.split(", ");
        this.ln = splits[0];
        this.fn = splits[1];
        this.handicap = h;
    }

    Golfer(String f, String l, int h){
        this.fn = f;
        this.ln = l;
        this.handicap = h;
    }

    public String getFn() {
        return fn;
    }

    public void setFn(String fn) {
        this.fn = fn;
    }

    public String getLn() {
        return ln;
    }

    public void setLn(String ln) {
        this.ln = ln;
    }

    public int getHandicap() {
        return handicap;
    }

    public void setHandicap(int handicap) {
        this.handicap = handicap;
    }

    public String toString(){
        return this.getFn() + " " + this.getLn() + " has a handicap of " + this.getHandicap() + ".";
    }

    public int compareTo(Golfer g){
        return this.getHandicap() - g.getHandicap();
    }

}