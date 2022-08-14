defmodule BirdCount do
  def today([]) do
    nil
  end

  def today([head | _tail]) do
    head
  end

  def increment_day_count([]) do
    [1]
  end

  def increment_day_count([head | tail]) do
    [head + 1 | tail]
  end

  def has_day_without_birds?(list) do
    do_has_day_without_birds?(list)
  end

  defp do_has_day_without_birds?([]) do
    false
  end

  defp do_has_day_without_birds?([0 | _tail]) do
    true
  end

  defp do_has_day_without_birds?([_head | tail]) do
    do_has_day_without_birds?(tail)
  end

  def total(list) do
    do_total(list, 0)
  end

  def do_total([], total) do
    total
  end

  def do_total([head | tail], total) do
    do_total(tail, total + head)
  end

  def busy_days(list) do
    do_busy_days(list, 0)
  end

  def do_busy_days([], total) do
    total
  end

  def do_busy_days([head | tail], total) when head >= 5 do
    do_busy_days(tail, total + 1)
  end

  def do_busy_days([_ | tail], total) do
    do_busy_days(tail, total)
  end
end
