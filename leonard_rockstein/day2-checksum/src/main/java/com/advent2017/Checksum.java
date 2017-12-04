package com.advent2017;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Checksum {


    public static void main(String[] args) throws IOException {
        Checksum checksum = new Checksum();
        System.out.println("Checksum: " + checksum.calculateChecksum(checksum.readTsvAndPopulateDiffs("/spreadsheet.tsv")));
        System.out.println("Evenly divisible checksum: " + checksum.calculateChecksum(checksum.readTsvAndCalculateEvenDivisors("/spreadsheet.tsv")));

    }

    private List<Integer> readRow(String tsvLine) {
        return Arrays.asList(tsvLine.split("\t"))
                .stream()
                .map(t -> Integer.parseInt(t))
                .collect(Collectors.toList());
    }

    private Integer calculateDiff(String tsvLine) {
        List<Integer> row = readRow(tsvLine);
        Integer min = row.stream().mapToInt(i -> i).min().getAsInt();
        Integer max = row.stream().mapToInt(i -> i).max().getAsInt();
        return max-min;
    }

    private Integer calculateEvenDivisorsInRow(String tsvLine) {
        List<Integer> evens = new ArrayList<>();
        List<Integer> row = readRow(tsvLine).stream().sorted().collect(Collectors.toList());
        int rowSize = row.size();
        for (int i = 0; i < rowSize; i++) {
            for (int j = 0; j < rowSize; j++) {
                // don't want to divide two of the same numbers
                if (row.get(i) == row.get(j)) {
                    continue;
                }
                if ((row.get(i) % row.get(j) == 0)) {
                    evens.add(row.get(i)/row.get(j));
                }
            }
        }

        return evens.stream().mapToInt(i -> i).sum();

    }

    private List<Integer> readTsvAndPopulateDiffs(String fileName) throws IOException {
        List<Integer> diffs = new ArrayList<>();

        for (String line : this.readTsv(fileName)) {
            diffs.add(calculateDiff(line));
        }
        return diffs;

    }

    private List<Integer> readTsvAndCalculateEvenDivisors(String fileName) throws IOException {
        List<Integer> divisors = new ArrayList<>();

        for (String line : this.readTsv(fileName)) {
            divisors.add(calculateEvenDivisorsInRow(line));
        }
        return divisors;

    }

    private List<String> readTsv(String fileName) throws IOException {
        List<String> numbers = new ArrayList<>();

        InputStream is = Checksum.class.getResourceAsStream(fileName);
        BufferedReader reader = new BufferedReader(new InputStreamReader(is));
        String line;
        while ((line = reader.readLine()) != null) {
            numbers.add(line);
        }
        return numbers;

    }

    private Integer calculateChecksum(List<Integer> numbers) {
        return numbers.stream().mapToInt(i -> i).sum();
    }


}
