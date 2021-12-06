# frozen_string_literal: true

class Grid
  attr_reader :lines
  attr_accessor :grid

  def initialize
    @grid = Hash.new(0)
    @lines = File.readlines('input.txt').map { |line| line.split(' -> ') }
  end
end

def part1
  game = Grid.new
  game.lines.each do |line|
    x1 = line[0].split(',')[0].to_i
    y1 = line[0].split(',')[1].to_i
    x2 = line[1].split(',')[0].to_i
    y2 = line[1].split(',')[1].to_i
    x1, x2 = x2, x1 if x2 < x1
    y1, y2 = y2, y1 if y2 < y1
    if y1 == y2
      (x1..x2).each do |x|
        game.grid["#{x},#{y1}"] += 1
      end
    elsif x1 == x2
      (y1..y2).each do |y|
        game.grid["#{x1},#{y}"] += 1
      end
    end
  end
  count = 0
  game.grid.each { |_g, v| count += 1 if v > 1 }
  puts count
end

def part2
  game = Grid.new
  game.lines.each do |line|
    x1 = line[0].split(',')[0].to_i
    y1 = line[0].split(',')[1].to_i
    x2 = line[1].split(',')[0].to_i
    y2 = line[1].split(',')[1].to_i
    if y1 == y2
      x1, x2 = x2, x1 if x2 < x1
      (x1..x2).each do |x|
        game.grid["#{x},#{y1}"] += 1
      end
    elsif x1 == x2
      y1, y2 = y2, y1 if y2 < y1
      (y1..y2).each do |y|
        game.grid["#{x1},#{y}"] += 1
      end
    elsif x1 < x2 && y1 < y2
      x = x1
      y = y1
      while x <= x2 && y <= y2
        game.grid["#{x},#{y}"] += 1
        x += 1
        y += 1
      end
    elsif x1 < x2 && y1 > y2
      x = x1
      y = y1
      while x <= x2 && y >= y2
        game.grid["#{x},#{y}"] += 1
        x += 1
        y -= 1
      end
    elsif x1 > x2 && y1 < y2
      x = x1
      y = y1
      while x >= x2 && y <= y2
        game.grid["#{x},#{y}"] += 1
        x -= 1
        y += 1
      end
    elsif x1 > x2 && y1 > y2
      x = x1
      y = y1
      while x >= x2 && y >= y2
        game.grid["#{x},#{y}"] += 1
        x -= 1
        y -= 1
      end
    end
  end
  count = 0
  game.grid.each { |_g, v| count += 1 if v > 1 }
  puts count
end

part1
part2
