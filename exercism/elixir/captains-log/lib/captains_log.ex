defmodule CaptainsLog do
  @planetary_classes ["D", "H", "J", "K", "L", "M", "N", "R", "T", "Y"]
  @stardate_min 41000.0
  @stardate_max 42000.0

  def random_planet_class() do
    Enum.random(@planetary_classes)
  end

  def random_ship_registry_number() do
    number = Enum.random(1_000..9_999)
    "NCC-#{number}"
  end

  def random_stardate() do
    (@stardate_max - @stardate_min) * :rand.uniform() + @stardate_min
  end

  def format_stardate(stardate) do
    :io_lib.format("~.1f", [stardate]) |> IO.iodata_to_binary()
  end
end
