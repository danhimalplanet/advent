package com.advent2017;


import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Entropy {

    private static final String goodInput = "aa bb cc dd ee";
    private static final String badInput = "aa bb cc dd aa";

    public static void main(String[] args) {
        System.out.println("Number of valid passphrases: " + numberOfValidPassphrases(goodInput));
        System.out.println("Good input: " + goodInput + ": " + validPassphrase(goodInput));
        System.out.println("Bad input: " + badInput + ": " + validPassphrase(badInput));

    }

    public static int numberOfValidPassphrases(String input) {
        return 1;
    }

    public static boolean validPassphrase(String passphrase) {
        Map<String, Boolean> seen = new HashMap<>();

        String[] words = passphrase.split("\\s");

        for (String word : Arrays.asList(words)) {
            if (seen.containsKey(word)) {
                return false;
            }
            seen.put(word, true);
        }

        return true;

    }

}
