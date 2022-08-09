defmodule Darts do
  @type position :: {number, number}

  @doc """
  Calculate the score of a single dart hitting a target
  """
  @spec score(position) :: integer
  def score({x, y}) do
    r = x * x + y * y

    cond do
      r > 100 -> 0
      r > 25 -> 1
      r > 1 -> 5
      true -> 10
    end
  end
end
