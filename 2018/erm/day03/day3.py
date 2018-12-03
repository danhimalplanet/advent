import itertools
from dataclasses import dataclass


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
        for y, x in itertools.product(self.pos_height_range, self.pos_width_range):
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

    grid_size = 2000
    grid_range = range(grid_size)
    grid = [[0] * grid_size for _ in grid_range]
    result_a = 0

    for claim in claims:
        for y, x in claim:
            grid[y][x] += 1

    for y, x in itertools.product(grid_range, grid_range):
        if grid[y][x] > 1:
            result_a += 1

    result_b = None

    for claim in claims:
        i = 0
        for y, x in claim:
            i += grid[y][x]
        if i == claim.size:
            result_b = claim.id
            break

    print(f"Part A: {result_a}")
    print(f"Part B: {result_b}")


if __name__ == "__main__":
    main()
