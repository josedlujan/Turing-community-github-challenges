package com.challenges;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Hello world!
 */
public final class App {
    public static int highestDigit(String s) {
        Pattern p = Pattern.compile("\\d+");
        Matcher m = p.matcher(s);
        if (!m.matches())
            return -1;

        int largest = -1, current = -1;
        for (int j = 0; j < s.length(); j++) {
            if ((current = Integer.parseInt(s.charAt(j) + "")) > largest)
                largest = current;
        }
        return largest;
    }

    public static boolean match(String s, String c) {
        if (s.length() != c.length())
            return false;
        return s.toLowerCase().equals(c.toLowerCase());
    }

    /**
     * Says hello to the world.
     * 
     * @param args The arguments of the program.
     */
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            for (int i = 0; i < 7; i++) {
                String s = sc.next();
                String c = sc.next();
                if ((match(s, c)))
                    System.out.println("True");
                else
                    System.out.println("False");
            }

            for (int i = 0; i < 7; i++) {
                String s = sc.next();
                int digit;
                if ((digit = highestDigit(s)) > -1)
                    System.out.println("largest: " + digit);
                else
                    System.out.println("please input digits only");
            }

            System.out.println("thats it, 7 times each only..");
        } catch (Exception e) {
            // TODO: handle exception
        }
    }
}
