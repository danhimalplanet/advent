package com.advent2017;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Jumps {
    
    
    public static void main(String[] args) throws IOException {
        String file = args[0];
        Jumps jumps = new Jumps();
    
        int[] localJump = jumps.jumpList(file);
        Integer jumpListSize = localJump.length;
        System.out.println("Jump list size: " + jumpListSize);
        boolean keepJumping = true;
        int numberOfJumps = 0;
        int i = 0;
        while (keepJumping) {
            try {
              //  System.out.println("*************");
              //  System.out.println("Initial Jump list " + Arrays.stream(jumps.jumpList()).mapToObj(String::valueOf).collect(Collectors.joining(",")));
                int jumpValue = localJump[i];
    
                int current = i;
                int nextJump = current + jumpValue;
             //   System.out.println("Current index " + current + ", " + "Jump size " + jumpValue + ", " + "Jumping from " + current + " to " + nextJump + ", Value at jump: " + localJump[nextJump]);
                int previous = current;
                i = nextJump;
    
              //  current += 1;
                localJump[previous] += 1;
                numberOfJumps++;
    
             //   System.out.println("Incremented previous jump value from " + previous + " to " + current);
             //   System.out.println("Modified Jump list " + Arrays.stream(localJump).mapToObj(String::valueOf).collect(Collectors.joining(",")));
    
             //   System.out.println("*************");
            } catch (IndexOutOfBoundsException e) {
                System.out.println("Jumped out of bounds in " + numberOfJumps);
                keepJumping = false;
            }
        }
    }
    
    private List<Integer> readFile(String fileName) throws IOException {
        List<Integer> lines = new ArrayList<>();
        
        InputStream is = Jumps.class.getResourceAsStream(fileName);
        BufferedReader reader = new BufferedReader(new InputStreamReader(is));
        String line;
        while ((line = reader.readLine()) != null) {
            lines.add(Integer.parseInt(line));
        }
        return lines;
        
    }
    
    public int[] jumpList(String file) throws IOException {
        List<Integer> ints = this.readFile("/" + file);//{0, 3, 0, 1, -3};
        int[] jumps = new int[ints.size()];
        // groce
        for (int i=0; i<ints.size(); i++) {
            jumps[i] = ints.get(i);
        }
        
        return jumps;
    }
    
    
}
