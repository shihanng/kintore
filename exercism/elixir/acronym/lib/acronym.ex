defmodule Acronym do
  @doc """
  Generate an acronym from a string.
  "This is a string" => "TIAS"
  """
  @spec abbreviate(String.t()) :: String.t()
  def abbreviate(string) do
    String.replace(string, ~r"[^[:alnum:][:space:]-]", "")
    |> String.split(~r"[\s-]+")
    |> join("")
  end

  defp join([head | tail], abbr) do
    <<char::binary-size(1)>> <> _ = head
    join(tail, abbr <> String.upcase(char))
  end

  defp join([], abbr), do: abbr
end
