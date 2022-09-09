# Use the Plot struct as it is provided
defmodule Plot do
  @enforce_keys [:plot_id, :registered_to]
  defstruct [:plot_id, :registered_to]
end

defmodule CommunityGarden do
  def start(opts \\ []) do
    Agent.start(fn -> %{next: 1, plots: []} end, opts)
  end

  def list_registrations(pid) do
    Agent.get(pid, fn %{plots: list} -> list end)
  end

  def register(pid, register_to) do
    next = Agent.get(pid, fn %{next: next} -> next end)
    plot = %Plot{plot_id: next, registered_to: register_to}

    Agent.update(pid, fn %{next: next, plots: plots} ->
      %{next: next + 1, plots: [plot | plots]}
    end)

    plot
  end

  def release(pid, plot_id) do
    Agent.update(pid, fn %{plots: plots} = state ->
      %{state | plots: Enum.reject(plots, fn %Plot{plot_id: id} -> id == plot_id end)}
    end)

    :ok
  end

  def get_registration(pid, plot_id) do
    Agent.get(pid, fn %{plots: plots} ->
      Enum.find(plots, {:not_found, "plot is unregistered"}, fn %Plot{plot_id: id} ->
        id == plot_id
      end)
    end)
  end
end
