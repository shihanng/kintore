defmodule Username do
  def sanitize(username) do
    do_sanitize(username, '')
  end

  defp do_sanitize([], sanitized) do
    sanitized
  end

  defp do_sanitize([first_char | rest], sanitized) do
    case first_char do
      ?_ -> do_sanitize(rest, sanitized ++ '_')
      ?ä -> do_sanitize(rest, sanitized ++ 'ae')
      ?ö -> do_sanitize(rest, sanitized ++ 'oe')
      ?ü -> do_sanitize(rest, sanitized ++ 'ue')
      ?ß -> do_sanitize(rest, sanitized ++ 'ss')
      c when c < ?a or c > ?z -> do_sanitize(rest, sanitized)
      _ -> do_sanitize(rest, sanitized ++ [first_char])
    end
  end
end
