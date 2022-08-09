defmodule GuessingGame do
  def compare(secret_number) do
    compare(secret_number, :no_guess)
  end

  def compare(_secret_number, :no_guess) do
    "Make a guess"
  end

  def compare(secret_number, guess) do
    compare_response(secret_number - guess)
  end

  def compare_response(0) do
    "Correct"
  end

  def compare_response(diff) when diff == 1 or diff == -1 do
    "So close"
  end

  def compare_response(diff) when diff > 0 do
    "Too low"
  end

  def compare_response(diff) when diff < 0 do
    "Too high"
  end
end
