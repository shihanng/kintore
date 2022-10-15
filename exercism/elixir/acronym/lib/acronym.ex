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
    join(tail, abbr <> String.upcase(String.first(head)))
  end

  defp join([], abbr), do: abbr
end
