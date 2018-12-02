# Day 1: Chronal Calibration

import itertools


def main() -> None:
    with open("data.txt", "r") as f:
        input_data = [int(s) for s in f.readlines()]

    result_a = sum(input_data)
    result_b = None
    frequency = 0
    seen = set()
    i = itertools.cycle(input_data)

    while result_b is None:
        frequency += next(i)
        if frequency in seen:
            result_b = frequency
        seen.add(frequency)

    print(f"Part A: {result_a}")
    print(f"Part B: {result_b}")


if __name__ == "__main__":
    main()
