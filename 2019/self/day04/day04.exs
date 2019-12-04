defmodule Day04 do
  @start 231_832
  @stop 767_346

  # [1, 2, 3, 4, 5, 6] -> [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
  def to_pairs(ls, lsls \\ [])
  def to_pairs([_], lsls), do: Enum.reverse(lsls)
  def to_pairs([one, two | rest], lsls), do: to_pairs([two | rest], [[one, two] | lsls])

  def alwaysinc(number) do
    number
    |> Integer.digits()
    |> to_pairs()
    |> Enum.all?(fn [a, b] -> a <= b end)
  end

  def haspairs(number, part) do
    digits = Integer.digits(number)

    counter =
      MapSet.new(digits)
      |> MapSet.to_list()
      |> Enum.map(fn digit -> {digit, Enum.count(digits, fn x -> x == digit end)} end)
      |> Map.new()

    case part do
      1 ->
        Enum.any?(Map.values(counter), fn val -> val >= 2 end)

      2 ->
        Enum.any?(Map.values(counter), fn val -> val == 2 end)
    end
  end

  def part(start, stop, _part, count) when start == stop, do: count

  def part(start, stop, part, count) do
    if alwaysinc(start) and haspairs(start, part) do
      part(start + 1, stop, part, count + 1)
    else
      part(start + 1, stop, part, count)
    end
  end

  def run() do
    {uSecs, val} = :timer.tc(Day04, :part, [@start, @stop, 1, 0])
    IO.puts("part1: #{val} in #{uSecs} microseconds")
    {uSecs, val} = :timer.tc(Day04, :part, [@start, @stop, 2, 0])
    IO.puts("part2: #{val} in #{uSecs} microseconds")
  end
end

Day04.run()

# run as: elixir day04.exs or iex day04.exs (interactive)
