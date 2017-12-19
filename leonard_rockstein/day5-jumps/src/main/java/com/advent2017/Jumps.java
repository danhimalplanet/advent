package com.advent2017;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Jumps {
    
    
    public static void main(String[] args) {
        Jumps jumps = new Jumps();
        
        Integer jumpListSize = jumps.jumpList().length;
        System.out.println("Jump list size: " + jumpListSize);
        int[] localJump = jumps.jumpList();
        boolean keepJumping = true;
        int numberOfJumps = 1;
        int i = 0;
        while (keepJumping) {
            try {
                System.out.println("*************");
                System.out.println("Initial Jump list " + Arrays.stream(jumps.jumpList()).mapToObj(String::valueOf).collect(Collectors.joining(",")));
                int jumpValue = localJump[i];
    
                int current = i;
                int nextJump = current + jumpValue;
                System.out.println("Current index " + current + ", " + "Jump size " + jumpValue + ", " + "Jumping from " + current + " to " + nextJump + ", Value at jump: " + localJump[nextJump]);
                int previous = current;
                i = nextJump;
    
                current += 1;
                localJump[previous] += 1;
                numberOfJumps++;
    
                System.out.println("Incremented previous jump value from " + previous + " to " + current);
                System.out.println("Modified Jump list " + Arrays.stream(localJump).mapToObj(String::valueOf).collect(Collectors.joining(",")));
    
                System.out.println("*************");
            } catch (IndexOutOfBoundsException e) {
                System.out.println("Jumped out of bounds in " + numberOfJumps);
                keepJumping = false;
            }
        }
    }
    
    public int[] jumpList() {
        int[] jumps = {0, 3, 0, 1, -3};
        
        return jumps;
    }
    
    
}
