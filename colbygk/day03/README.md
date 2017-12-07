## AoC Day 3 - Ulam Spirals

### Part1

These spirals can be analyzed as part of a recurrence relation

```
  a_0 = 1
  a_n = (8*n) + a_(n-1)
```

This can narrow the range of a distance search by computing which spiral
a number **b** exists on, then using modulo arithmetic compute the distance for
the number on that particular spiral given by example for 25 < **b** < 50:

```
1       2       3       4       5       0       1
6       5       4       3       4       5       6
n      n-1     n-2     n-3     n-2     n-1      n
```

And for 49 < **b** < 82

```
1       2       3       4       5       6       7       0       1
8       7       6       5       4       5       6       7       8
n      n-1     n-2     n-3     n-4     n-3     n-2     n-1      n
```

To build and run:

```
cat part1
go build
./part1
```
