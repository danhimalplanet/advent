defmodule Day08 do
  @width 25
  @height 6

  defp input(path) do
    File.read!(path)
    |> String.trim()
    |> String.graphemes()
    |> Stream.chunk_every(@width * @height)
  end

  defp count(layer, item) do
    Enum.count(layer, &(&1 == item))
  end

  defp fewestzeros(layers) do
    layeridx =
      layers
      |> Stream.with_index()
      |> Stream.map(fn {layer, index} -> {count(layer, "0"), index} end)
      |> Enum.sort(fn {a, _}, {b, _} -> a < b end)
      |> List.first()
      |> elem(1)

    Enum.at(layers, layeridx)
  end

  def part1(imagedata) do
    zerolayer = fewestzeros(imagedata)

    count(zerolayer, "1") * count(zerolayer, "2")
  end

  defp fillgrid([], grid), do: grid

  defp fillgrid([layer | layers], grid) do
    grid =
      layer
      |> Stream.zip(grid)
      |> Stream.map(fn {pixel, gpixel} ->
        case pixel do
          "2" -> gpixel
          "1" -> "#"
          "0" -> " "
        end
      end)

    fillgrid(layers, grid)
  end

  def part2(imagedata) do
    imagedata
    |> Enum.reverse()
    |> fillgrid(List.duplicate("2", @width * @height))
    |> Stream.chunk_every(@width)
    |> Enum.map(&Enum.join/1)
  end

  def run(path \\ "/tmp/8.input") do
    imagedata = input(path)

    {uSecs, val} = :timer.tc(Day08, :part1, [imagedata])
    IO.puts("part 1 took #{uSecs} usecs for #{val}")

    {uSecs, val} = :timer.tc(Day08, :part2, [imagedata])
    IO.puts("part 1 took #{uSecs} usecs for")
    Enum.each(val, &IO.puts/1)
  end
end

Day08.run()
