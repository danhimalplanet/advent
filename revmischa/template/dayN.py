from .. import Computer, main


class DayN(Computer):
    def __init__(self, structure):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.input = structure

    def run_part1(self):
        pass

    def run_part2(self):
        pass

if __name__ == '__main__':
    main(DayN)
