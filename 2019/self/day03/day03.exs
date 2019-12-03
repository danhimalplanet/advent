defmodule Day03 do
  @moduledoc """
  Day 3, Advent of Code.
  """

  @doc """
  Calculate the Manhattan distance from the origin to the nearest
  intersection.
  """
  def part1(path) do
    [path1, path2] =
      input(path)
      |> Enum.map(&path/1)
      |> Enum.map(&Enum.map(&1, fn {x, y, _steps} -> {x, y} end))
      |> Enum.map(&MapSet.new/1)

    MapSet.intersection(path1, path2)
    |> MapSet.to_list()
    |> Enum.map(&distance/1)
    |> Enum.sort()
    |> Enum.drop(1)
    |> List.first()
  end

  @doc """
  Calculate the fewest number of steps both wires take to reach an
  intersection.
  """
  def part2(path) do
    [m1, m2] =
      input(path)
      |> Enum.map(&path/1)
      |> Enum.map(&Enum.map(&1, fn {x, y, steps} -> %{{x, y} => steps} end))
      |> Enum.map(&Enum.reduce(&1, %{}, fn x, acc -> Map.merge(acc, x) end))

    MapSet.intersection(MapSet.new(Map.keys(m1)), MapSet.new(Map.keys(m2)))
    |> MapSet.to_list()
    |> Enum.map(fn {x, y} = k -> {x, y, Map.get(m1, k) + Map.get(m2, k)} end)
    |> Enum.sort_by(fn {_x, _y, size} -> size end)
    |> Enum.drop(1)
    |> List.first()
    |> elem(2)
  end

  @doc """
  Take a direction and number of steps in the format {"X", steps} and
  a position and number of steps taken so far in the format {x, y,
  sofarsteps}.  Return the ending position (with steps) along with a
  list of steps taken.

  ## Examples

    iex> Day03.move({"R", 5}, {10, 20, 30})
    {{15, 20, 35},
     [
       {10, 20, 30},
       {11, 20, 31},
       {12, 20, 32},
       {13, 20, 33},
       {14, 20, 34},
       {15, 20, 35}
     ]}
  """
  def move({direction, steps} = _move, {x, y, prevsteps} = _pos) do
    case direction do
      "R" ->
        {{x + steps, y, prevsteps + steps},
         for(step <- 0..steps, do: {x + step, y, prevsteps + step})}

      "L" ->
        {{x - steps, y, prevsteps + steps},
         for(step <- 0..steps, do: {x - step, y, prevsteps + step})}

      "U" ->
        {{x, y + steps, prevsteps + steps},
         for(step <- 0..steps, do: {x, y + step, prevsteps + step})}

      "D" ->
        {{x, y - steps, prevsteps + steps},
         for(step <- 0..steps, do: {x, y - step, prevsteps + step})}
    end
  end

  defp path(moves, pos \\ {0, 0, 0}, already \\ [])

  defp path([], _endpos, fullpath), do: fullpath

  defp path([firstmove | moves], pos, alreadypath) do
    {newpos, wirepath} = move(firstmove, pos)
    path(moves, newpos, alreadypath ++ wirepath)
  end

  defp distance({x, y} = _pos), do: abs(x) + abs(y)

  defp input(path) do
    File.read!(path)
    |> String.split()
    |> Enum.map(&String.split(&1, ","))
    # ugly
    |> Enum.map(
      &Enum.map(
        &1,
        fn x ->
          String.split_at(x, 1)
          |> (fn {dir, steps} -> {dir, String.to_integer(steps, 10)} end).()
        end
      )
    )
  end

  @doc """
  Main entry point.
  """
  def run(path \\ "input.txt") do
    IO.puts(part1(path))
    IO.puts(part2(path))
  end
end

Day03.run()

# run as: elixir day03.exs or iex day03.exs (interactive)
