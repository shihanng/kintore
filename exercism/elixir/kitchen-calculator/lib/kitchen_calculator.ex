defmodule KitchenCalculator do
  def get_volume({_, volume}) do
    volume
  end

  def to_milliliter({from_unit, volume}), do: {:milliliter, volume * in_milliliter(from_unit)}

  def from_milliliter({:milliliter, volume}, to_unit) do
    {to_unit, volume / in_milliliter(to_unit)}
  end

  def convert(volume_pair, unit) do
    volume_pair |> to_milliliter |> from_milliliter(unit)
  end

  defp in_milliliter(:cup), do: 240
  defp in_milliliter(:fluid_ounce), do: 30
  defp in_milliliter(:teaspoon), do: 5
  defp in_milliliter(:tablespoon), do: 15
  defp in_milliliter(:milliliter), do: 1
end
