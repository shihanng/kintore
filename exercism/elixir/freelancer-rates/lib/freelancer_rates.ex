defmodule FreelancerRates do
  @daily_rate 8.0
  @billable_days 22

  def daily_rate(hourly_rate) do
    hourly_rate * @daily_rate
  end

  def apply_discount(before_discount, discount) do
    before_discount - before_discount * discount / 100.0
  end

  def monthly_rate(hourly_rate, discount) do
    (daily_rate_after_discount(hourly_rate, discount) * @billable_days) |> Float.ceil(0) |> trunc
  end

  def days_in_budget(budget, hourly_rate, discount) do
    (budget / daily_rate_after_discount(hourly_rate, discount)) |> Float.floor(1)
  end

  defp daily_rate_after_discount(hourly_rate, discount) do
    hourly_rate |> daily_rate |> apply_discount(discount)
  end
end
