defmodule BoutiqueSuggestions do
  def get_combinations(tops, bottoms, opt \\ [])

  def get_combinations(tops, bottoms, maximum_price: maximum_price) do
    for top <- tops,
        bottom <- bottoms,
        top.base_color != bottom.base_color and top.price + bottom.price <= maximum_price do
      {top, bottom}
    end
  end

  def get_combinations(tops, bottoms, _opt) do
    get_combinations(tops, bottoms, maximum_price: 100.0)
  end
end
