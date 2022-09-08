public class SolutionChallenge1 {
  public static void main(String[] args) {
    new SolutionChallenge1().solve();
  }

  public void solve() {
    System.out.println(highestDigit(12899));
    System.out.println(highestDigit(8123));
    System.out.println(highestDigit(193));
    System.out.println(highestDigit(1));

    System.out.println(match("Jose", "JoSe"));
    System.out.println(match("water", "wait"));
    System.out.println(match("JOHN", "JOHn"));
    System.out.println(match("ElEmEnTs", "eLeMeNtS"));
  }

  /**
   * Return the highest digit of the number
   * 
   * @param number
   * @return
   */
  public int highestDigit(int number) {
    int highestDigit = 0;

    while (number > 0) {
      int lastDigit = number % 10;
      highestDigit = Math.max(lastDigit, highestDigit);
      number /= 10;
    }

    return highestDigit;
  }

  /**
   * Compares two strings ignoring case considerations
   * 
   * @param firstString
   * @param secondString
   * @return
   */
  public boolean match(String firstString, String secondString) {
    return firstString.equalsIgnoreCase(secondString);
  }
}