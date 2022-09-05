defmodule Newsletter do
  def read_emails(path) do
    {:ok, binary} = File.read(path)
    binary |> String.split()
  end

  def open_log(path) do
    File.open!(path, [:write])
  end

  def log_sent_email(pid, email) do
    IO.binwrite(pid, email <> "\n")
  end

  def close_log(pid) do
    File.close(pid)
  end

  def send_newsletter(emails_path, log_path, send_fun) do
    log = open_log(log_path)

    read_emails(emails_path)
    |> Enum.each(fn email ->
      case send_fun.(email) do
        :ok ->
          log_sent_email(log, email)

        _ ->
          nil
      end
    end)

    close_log(log)
  end
end
