package com.advent2017;


import java.io.*;
import java.util.Scanner;

public class Checksum {

    public static void main(String[] args) throws IOException {
        Checksum checksum = new Checksum();
        System.out.println(checksum.readTsv("/spreadsheet.tsv"));

    }

    private String readTsv(String fileName) throws IOException {

        StringBuilder result = new StringBuilder("");
        InputStream is = Checksum.class.getResourceAsStream(fileName);
        BufferedReader reader = new BufferedReader(new InputStreamReader(is));
        String line;
        while ((line = reader.readLine()) != null) {
            result.append(line).append("\n");
        }
        return result.toString();

    }


}
