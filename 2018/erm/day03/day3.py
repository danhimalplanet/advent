from dataclasses import dataclass
from collections import Counter


@dataclass
class Claim:
    id: str
    offset_x: int
    offset_y: int
    width: int
    height: int

    @property
    def pos_height_range(self) -> range:
        return range(self.offset_y, self.offset_y + self.height)

    @property
    def pos_width_range(self) -> range:
        return range(self.offset_x, self.offset_x + self.width)

    @property
    def size(self):
        return self.width * self.height

    def __iter__(self) -> None:
        for y in self.pos_height_range:
            for x in self.pos_width_range:
                yield y, x


def main() -> None:

    with open("data.txt", "r") as f:
        input_data = [s.strip() for s in f.readlines()]
        claims = []
        for i in input_data:
            _claim = i.split()
            offset_x, offset_y = _claim[2].replace(":", "").split(",")
            width, height = _claim[3].split("x")
            claim = Claim(
                id=_claim[0],
                offset_x=int(offset_x),
                offset_y=int(offset_y),
                width=int(width),
                height=int(height),
            )
            claims.append(claim)

    result_a = 0

    pos_counter = Counter([pos for claim in claims for pos in claim])
    result_a = sum([1 for i in pos_counter.values() if int(i) > 1])

    result_b = None

    for claim in claims:
        if all(pos_counter[pos] < 2 for pos in claim):
            result_b = claim.id
            break

    print(f"Part A: {result_a}")
    print(f"Part B: {result_b}")


if __name__ == "__main__":
    main()
