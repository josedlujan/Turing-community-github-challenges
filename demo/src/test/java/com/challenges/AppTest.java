package com.challenges;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * Unit test for simple App.
 */
class AppTest {
    /**
     * Rigorous Test.
     */
    @Test
    void testDigits() {
        assertEquals(App.highestDigit(12899 + ""), 9);
        assertEquals(App.highestDigit(8123 + ""), 8);
        assertEquals(App.highestDigit(193 + ""), 9);
        assertEquals(App.highestDigit(1 + ""), 1);
    }

    @Test
    void testCaseInsensitiveComparisonChallenge() {
        assertEquals(App.match("Jose", "JoSe"), true);
        assertEquals(App.match("water", "wait"), false);
        assertEquals(App.match("JOHN", "JOHn"), true);
        assertEquals(App.match("ElEmEnTs", "eLeMeNtS"), true);
    }
}
