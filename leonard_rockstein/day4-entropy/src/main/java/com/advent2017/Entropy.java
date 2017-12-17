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
        System.out.println("Number of valid passphrases: " + entropy.numberOfNonRepeatingPassphrases());
        System.out.println("Number of valid non anagram passphrases: " + entropy.numberOfValidPassphrases());
        
    }
    
    public int numberOfValidPassphrases() throws IOException {
        List<String> validPassphrases = new ArrayList<>();
        for (String line : this.nonRepeatingPassphrases()) {
            if (!this.containsAnagram(line)) {
                validPassphrases.add(line);
            }
        }
        
        return validPassphrases.size();
    }
    
    public List<String> nonRepeatingPassphrases() throws IOException {
        List<String> nonRepeating = new ArrayList<>();
        for (String line : this.readFile("/passphrases.txt")) {
            if (this.nonRepeatingPassphrase(line)) {
                nonRepeating.add(line);
            }
        }
        return nonRepeating;
    }
    
    public int numberOfNonRepeatingPassphrases() throws IOException {
        return this.nonRepeatingPassphrases().size();
    }
    
    public boolean containsAnagram(String line) {
        Map<String, String> anagramHashes = new HashMap<>();
        String[] wordsInLine = line.split("\\s");
        
        for (int i = 0; i < wordsInLine.length; i++) {
            String baseWord = wordsInLine[i].toLowerCase();
            anagramHashes.put(hashAnagram(baseWord), baseWord);
            for (String comparisonWord : Arrays.copyOfRange(wordsInLine, i+1, wordsInLine.length)) {
                if (anagramHashes.containsKey(hashAnagram(comparisonWord.toLowerCase()))) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    public String hashAnagram(String word) {
        char[] characters = word.toCharArray();
        Arrays.sort(characters);
        return new String(characters);
    }
    
    public boolean nonRepeatingPassphrase(String passphrase) {
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
    
    private List<String> readFile(String fileName) throws IOException {
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
