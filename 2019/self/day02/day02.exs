defmodule Day02 do
  def part1(intcode \\ input(), noun \\ 12, verb \\ 2) do
    intcode
    |> List.replace_at(1, noun)
    |> List.replace_at(2, verb)
    |> runloop()
    |> Enum.at(0)
  end

  # not happy with how this works
  def part2(intcode \\ input()) do
    me = self()

    for noun <- 0..100,
        verb <- 0..100 do
      spawn(fn -> send(me, {part1(intcode, noun, verb), noun * 100 + verb}) end)
    end

    receive do
      {answer, nv} when answer == 19_690_720 ->
        IO.puts(nv)
        exit(:normal)
    end
  end

  defp input() do
    with {:ok, contents} <- File.read("input.txt") do
      contents
      |> String.trim()
      |> String.split(",")
      |> Enum.map(&String.to_integer/1)
    else
      _ ->
        IO.puts("could not read input file")
        exit(:sad)
    end
  end

  defp runloop(arr, pos \\ 0) do
    case Enum.at(arr, pos) do
      99 ->
        arr

      1 ->
        arr
        |> op(pos, &(&1 + &2))
        |> runloop(pos + 4)

      2 ->
        arr
        |> op(pos, &(&1 * &2))
        |> runloop(pos + 4)
    end
  end

  defp op(arr, pos, opfunc) do
    with a <- Enum.at(arr, pos + 1),
         b <- Enum.at(arr, pos + 2),
         dst <- Enum.at(arr, pos + 3) do
      List.replace_at(arr, dst, opfunc.(Enum.at(arr, a), Enum.at(arr, b)))
    end
  end
end

IO.puts(Day02.part1())
IO.puts(Day02.part2())

# run as: elixir day02.exs or iex day02.exs (interactive)
