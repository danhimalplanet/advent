from .computer import Computer  # noqa

def main(input_: str, computer_cls: Computer):
    computer = computer_cls.new_from_puzzle_input(input_)
    answer_1 = computer.run_part1()
    print(f'Part I Answer: {answer_1}')
    answer_2 = computer.run_part2()
    print(f'Part II Answer: {answer_2}')
