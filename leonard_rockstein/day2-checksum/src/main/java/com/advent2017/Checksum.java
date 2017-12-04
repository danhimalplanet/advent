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

    private List<Integer> readTsvAndPopulateDiffs(String fileName) throws IOException {
        List<Integer> diffs = new ArrayList<>();

        InputStream is = Checksum.class.getResourceAsStream(fileName);
        BufferedReader reader = new BufferedReader(new InputStreamReader(is));
        String line;
        while ((line = reader.readLine()) != null) {
            diffs.add(calculateDiff(line));
        }
        return diffs;

    }

    private Integer calculateChecksum(List<Integer> diffs) {
        return diffs.stream().mapToInt(i -> i).sum();
    }


}
