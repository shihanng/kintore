defmodule Lasagna do
  def expected_minutes_in_oven, do: 40

  def remaining_minutes_in_oven(current) do
    expected_minutes_in_oven() - current
  end

  def preparation_time_in_minutes(layer), do: 2 * layer

  def total_time_in_minutes(layer, current) do
    preparation_time_in_minutes(layer) + current
  end

  def alarm, do: "Ding!"
end
