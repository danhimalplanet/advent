defmodule Day06 do

  @doc """
  Starting from a satellite, trace the path back to COM.

  Return both the path to COM and the number of orbits.
  """
  def count(satellite, orbits, path \\ [], n \\ 0) do
    with {:ok, around} <- Map.fetch(orbits, satellite) do
      count(around, orbits, [around | path], n + 1)
    else
      _ -> {Enum.reverse(path), n}
    end
  end

  def part1(orbits) do
    Enum.reduce(orbits, 0, fn {satellite, _}, acc -> acc + elem(count(satellite, orbits), 1) end)
  end

  @doc """
  Count the number of transfers between you and Santa.

  This does more work than necessary.
  """
  def count_transfers([you_cur | you_rest], santa_path, transfers \\ 0) do
    if idx = Enum.find_index(santa_path, fn p -> p == you_cur end) do
      transfers + idx
    else
      count_transfers(you_rest, santa_path, transfers + 1)
    end
  end

  def part2(orbits) do
    you_orbit = Enum.find_value(orbits, fn {k, v} -> k == "YOU" and v end)
    you_path = count(you_orbit, orbits, [you_orbit]) |> elem(0)


    santa_orbits = Enum.find_value(orbits, fn {k, v} -> k == "SAN" and v end)
    santa_path = count(santa_orbits, orbits, [santa_orbits]) |> elem(0)

    count_transfers(you_path, santa_path)
  end

  defp input(path) do
    File.read!(path)
    |> String.split()
    |> Enum.map(&String.split(&1, ")"))
    |> Enum.map(fn [center, satellite] -> {satellite, center} end)
    |> Map.new()
  end

  def run(fname \\ "/tmp/6.input") do
    orbits = input(fname)
    IO.puts(part1(orbits))
    IO.puts(part2(orbits))
  end
end

Day06.run()
