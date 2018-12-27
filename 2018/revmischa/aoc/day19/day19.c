#include <stdio.h>

typedef unsigned int reg;

void print_regs(reg regs[6], unsigned int loops) {
    for (int i = 0; i < 6; i++)
        printf("regs[%d]=%u\n", i, regs[i]);
    printf("loops=%u\n", loops);
}

int main() {
    // initial condition when loop begins
    reg r[] = {0, 1, 3, 1, 10551275, 0};
    unsigned int loops = 0;

    while (1) {  // end when r1 > r4
        /* loops++; */

        /* if (loops % 1000000000 == 0) { */
        /*     print_regs(r, loops); */
        /* } */

        r[5] = r[1] * r[3];  // mulr 1 3 5
        if (r[4] == r[5]) {  // eqrr 5 4 5 ....
            printf("inc 0\n");
            r[0] += r[1];  // addr 1 0 0
        }

        r[3]++;  // addi 3 1 3

        if (r[3] > r[4]) {  // gtrr 3 4 5
            r[1]++;  // addi 1 1 1
            if (r[1] > r[4]) {  // gtrr 1 4 5
                break;  // end condition
            }

            r[3] = 1;  // seti 1 4 3  (loop restart if not end condition)
            continue;
        } else {
            continue;  // seti 2 4 2 - restart loop
        }
    }

    print_regs(r, loops);
}
