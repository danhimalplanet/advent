def main() -> None:

    with open("data.txt", "r") as f:
        input_data = [s.strip() for s in f.readlines()]

    result_a = []

    for line in input_data:
        res = []
        for i in line:
            if res:
                if res[-1] != i.swapcase():
                    res.append(i)
                else:
                    res.pop()
            else:
                res.append(i)

        result_a.extend(res)

    result_a = len(result_a)

    print(f"Part A: {result_a}")


if __name__ == "__main__":
    main()
