defmodule Day01 do
  def part1(mass \\ input()) do
    mass
    |> Enum.map(&calcfuel/1)
    |> Enum.sum()
  end

  def part2(mass \\ input()) do
    mass
    |> Enum.map(&calcfuel2/1)
    |> Enum.sum()
  end

  defp input() do
    with {:ok, contents} <- File.read("input.txt") do
      contents
      |> String.split()
      |> Enum.map(&String.to_integer/1)
    else
      _ ->
        IO.puts("could not read input file")
        exit(:sad)
    end
  end

  defp calcfuel(mass), do: div(mass, 3) - 2

  defp calcfuel2(mass, masses \\ [])

  defp calcfuel2(mass, masses) when mass <= 0, do: Enum.sum(masses)

  defp calcfuel2(mass, masses) do
    fuel = calcfuel(mass)
    calcfuel2(fuel, [fuel | masses])
  end
end

IO.puts("part1: #{Day01.part1()}")
IO.puts("part2: #{Day01.part2()}")

# run as: elixir day01.exs or iex day01.exs (interactive)
