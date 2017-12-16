package com.advent2017;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Entropy {


    public static void main(String[] args) throws IOException {
        Entropy entropy = new Entropy();
        System.out.println("Number of valid passphrases: " + entropy.numberOfValidPassphrases());

    }

    public int numberOfValidPassphrases() throws IOException {
        int validPassphrases = 0;
        for (String line : this.readTsv("/passphrases.txt")) {
            if (validPassphrase(line)) {
                validPassphrases += 1;
            }
        }
        return validPassphrases;
    }

    public boolean validPassphrase(String passphrase) {
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

    private List<String> readTsv(String fileName) throws IOException {
        List<String> lines = new ArrayList<>();

        InputStream is = Entropy.class.getResourceAsStream(fileName);
        BufferedReader reader = new BufferedReader(new InputStreamReader(is));
        String line;
        while ((line = reader.readLine()) != null) {
            lines.add(line);
        }
        return lines;

    }

}
