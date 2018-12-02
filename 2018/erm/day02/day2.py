# Day 2: Inventory Management System

from typing import Union


def has_count(line: str, n: int) -> bool:
    return [i for i in line if line.count(i) == n]


def compare_result(line_one: str, line_two: str) -> Union[str, None]:
    seen_missing = False
    result = []
    for s_one, s_two in zip(line_one, line_two):
        if s_one != s_two:
            if seen_missing:
                return None
            else:
                seen_missing = True
        else:
            result.append(s_one)
    return "".join(result)


def compare_lines(input_data: list) -> str:
    for line in input_data:
        for _line in input_data:
            if _line != line:
                result_b = compare_result(_line, line)
                if result_b:
                    return result_b


def main() -> None:
    two_count = 0
    three_count = 0

    with open("data.txt", "r") as f:
        input_data = [s.strip() for s in f.readlines()]

    for line in input_data:
        if has_count(line, 2):
            two_count += 1
        if has_count(line, 3):
            three_count += 1

    result_a = two_count * three_count
    result_b = None

    while result_b is None:
        result_b = compare_lines(input_data)

    print(f"Part A: {result_a}")
    print(f"Part B: {result_b}")


if __name__ == "__main__":
    main()
