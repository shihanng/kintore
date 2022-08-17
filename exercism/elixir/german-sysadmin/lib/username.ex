defmodule Username do
  def sanitize(username) do
    Enum.reduce(username, '', &sanitize_char/2)
  end

  defp sanitize_char(first_char, sanitized) do
    sanitized_char =
      case first_char do
        ?_ -> '_'
        ?ä -> 'ae'
        ?ö -> 'oe'
        ?ü -> 'ue'
        ?ß -> 'ss'
        c when c < ?a or c > ?z -> ''
        _ -> [first_char]
      end

    sanitized ++ sanitized_char
  end
end
