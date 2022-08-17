package Community_Github_Challenges_1.java_solutions;

public class Tester {
    public static void main(String[] args) {

        // let's test the solution for highest digit problem
        System.out.println(Challenge1.highestDigit(12899));
        System.out.println(Challenge1.highestDigit(8123) );
        System.out.println(Challenge1.highestDigit(193));
        System.out.println(Challenge1.highestDigit(1));

        // let's test the solution for case insensitive comparison
        System.out.println(Challenge2.match("Jose", "JoSe"));
        System.out.println(Challenge2.match("water", "wait"));
        System.out.println(Challenge2.match("JOHN", "JOHn"));
        System.out.println(Challenge2.match("ElEmEnTs", "eLeMeNtS"));
    }
}
