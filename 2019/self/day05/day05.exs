defmodule Mode do
  defstruct [:first, :second, :third]

  def mode(modestr) do
    %Mode{
      first: String.to_integer(String.at(modestr, 2)),
      second: String.to_integer(String.at(modestr, 1)),
      third: String.to_integer(String.at(modestr, 0))
    }
  end
end

defmodule Day05 do
  # modes
  @pos 0

  def input(path \\ "/tmp/5.input") do
    File.read!(path)
    |> String.trim()
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
  end

  def decode(opcode) do
    {modestr, opstr} =
      Integer.to_string(opcode)
      |> String.pad_leading(5, "0")
      |> String.split_at(3)

    {Mode.mode(modestr), String.to_integer(opstr)}
  end

  def args(intcode, a, %Mode{} = mode) do
    if mode.first == @pos do
      Enum.at(intcode, Enum.at(intcode, a))
    else
      Enum.at(intcode, a)
    end
  end

  def args(intcode, a, b, %Mode{} = mode) do
    first =
      if mode.first == @pos do
        Enum.at(intcode, Enum.at(intcode, a))
      else
        Enum.at(intcode, a)
      end

    second =
      if mode.second == @pos do
        Enum.at(intcode, Enum.at(intcode, b))
      else
        Enum.at(intcode, b)
      end

    {first, second}
  end

  def args(intcode, a, b, c, %Mode{} = mode) do
    first =
      if mode.first == @pos do
        Enum.at(intcode, Enum.at(intcode, a))
      else
        Enum.at(intcode, a)
      end

    second =
      if mode.second == @pos do
        Enum.at(intcode, Enum.at(intcode, b))
      else
        Enum.at(intcode, b)
      end

    third =
      if mode.third == @pos do
        Enum.at(intcode, Enum.at(intcode, c))
      else
        Enum.at(intcode, c)
      end

    {first, second, third}
  end

  def add({first, second}, dst, intcode) do
    intcode
    |> List.replace_at(dst, first + second)
  end

  def mul({first, second}, dst, intcode) do
    intcode
    |> List.replace_at(dst, first * second)
  end

  # always immediate
  def write(dst, user_input, intcode) do
    List.replace_at(intcode, dst, user_input)
  end

  def read(src, intcode) do
    IO.puts("read #{src}")
    intcode
  end

  def runloop(intcode, user_input, pc) do
    with {mode, op} <- decode(Enum.at(intcode, pc)) do
      case op do
        99 ->
          :ok

        1 ->
          intcode
          |> args(pc + 1, pc + 2, mode)
          |> add(Enum.at(intcode, pc + 3), intcode)
          |> runloop(user_input, pc + 4)

        2 ->
          intcode
          |> args(pc + 1, pc + 2, mode)
          |> mul(Enum.at(intcode, pc + 3), intcode)
          |> runloop(user_input, pc + 4)

        3 ->
          write(Enum.at(intcode, pc + 1), user_input, intcode)
          |> runloop(user_input, pc + 2)

        4 ->
          intcode
          |> args(pc + 1, mode)
          |> read(intcode)
          |> runloop(user_input, pc + 2)

        5 ->
          {first, newpc} = args(intcode, pc + 1, pc + 2, mode)

          if first != 0 do
            runloop(intcode, user_input, newpc)
          else
            runloop(intcode, user_input, pc + 3)
          end

        6 ->
          {first, newpc} = args(intcode, pc + 1, pc + 2, mode)

          if first == 0 do
            runloop(intcode, user_input, newpc)
          else
            runloop(intcode, user_input, pc + 3)
          end

        7 ->
          {first, second} = args(intcode, pc + 1, pc + 2, mode)
          r = if first < second, do: 1, else: 0

          List.replace_at(intcode, Enum.at(intcode, pc + 3), r)
          |> runloop(user_input, pc + 4)

        8 ->
          {first, second} = args(intcode, pc + 1, pc + 2, mode)
          r = if first == second, do: 1, else: 0

          List.replace_at(intcode, Enum.at(intcode, pc + 3), r)
          |> runloop(user_input, pc + 4)
      end
    end
  end

  def run(user_input, intcode \\ input()) do
    runloop(intcode, user_input, 0)
  end
end

Day05.run(1)
Day05.run(5)
