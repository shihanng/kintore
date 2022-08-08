defmodule LogLevel do
  def to_label(0, false) do
    :trace
  end

  def to_label(1, _) do
    :debug
  end

  def to_label(2, _) do
    :info
  end

  def to_label(3, _) do
    :warning
  end

  def to_label(4, _) do
    :error
  end

  def to_label(5, false) do
    :fatal
  end

  def to_label(_, _) do
    :unknown
  end

  def alert_recipient(level, legacy?) do
    to_label(level, legacy?) |> alert(legacy?)
  end

  defp alert(:error, _) do
    :ops
  end

  defp alert(:fatal, _) do
    :ops
  end

  defp alert(:unknown, true) do
    :dev1
  end

  defp alert(:unknown, _) do
    :dev2
  end

  defp alert(_, _) do
    false
  end
end
