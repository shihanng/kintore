defmodule ArmstrongNumber do
  @moduledoc """
  Provides a way to validate whether or not a number is an Armstrong number
  """

  @spec valid?(integer) :: boolean
  def valid?(number) do
    armstrong_num(number, 0, digit(number)) == number
  end

  defp armstrong_num(0, acc, _), do: acc

  defp armstrong_num(number, acc, exp) do
    acc = rem(number, 10) |> :math.pow(exp) |> Kernel.+(acc)
    armstrong_num(div(number, 10), acc, exp)
  end

  defp digit(0), do: 1

  defp digit(number) do
    :math.log10(number) |> trunc |> Kernel.+(1)
  end
end
