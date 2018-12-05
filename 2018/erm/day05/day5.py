def get_result(line) -> list:
    res = []
    for i in line:
        if res:
            if res[-1] != i.swapcase():
                res.append(i)
            else:
                res.pop()
        else:
            res.append(i)

    return res


def main() -> None:

    with open("data.txt", "r") as f:
        input_data = [s.strip() for s in f.readlines()]

    result_a = []
    result_b = 0
    results = {}

    for line in input_data:
        res = get_result(line)
        result_a.extend(res)
        for i in set(line.lower()):
            _line = line.replace(i, "").replace(i.upper(), "")
            results[i] = len(get_result(_line))

    result_a = len(result_a)
    result_b = min(results.values())

    print(f"Part A: {result_a}")
    print(f"Part B: {result_b}")


if __name__ == "__main__":
    main()
