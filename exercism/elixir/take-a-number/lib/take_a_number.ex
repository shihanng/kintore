defmodule TakeANumber do
  def start() do
    spawn(&loop/0)
  end

  defp loop(num \\ 0) do
    receive do
      {:report_state, sender_pid} -> send(sender_pid, num) |> loop()
      {:take_a_number, sender_pid} -> send(sender_pid, num + 1) |> loop()
      :stop -> nil
      _msg -> loop(num)
    end
  end
end
