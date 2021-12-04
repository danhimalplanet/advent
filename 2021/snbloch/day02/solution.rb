class Submarine
    attr_reader :moves, :position, :depth
    def initialize(part)
        @part = part
        @moves = File.readlines('input.txt').map! { |move| move = move.split }
        @position = 0
        @depth = 0
        @aim = 0
    end

    def move direction, value
        if @part == 'part1'
            if direction == 'forward'
                @position += value
            elsif direction == 'down'
                @depth += value
            elsif direction == 'up'
                @depth -= value
            end
        elsif @part == 'part2'
            if direction == 'forward'
                @position += value
                @depth += @aim * value
            elsif direction == 'down'
                @aim += value
            elsif direction == 'up'
                @aim -= value
            end
        end
    end
end

def part1
    sub = Submarine.new('part1')
    sub.moves.each { |m| sub.move(m[0], m[1].to_i) }
    puts sub.position * sub.depth
end

def part2
    sub = Submarine.new('part2')
    sub.moves.each { |m| sub.move(m[0], m[1].to_i) }
    puts sub.position * sub.depth
end

part1
part2