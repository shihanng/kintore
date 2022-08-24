defmodule DNA do
  @nucleotide_to_code %{?\s => 0b0000, ?A => 0b0001, ?C => 0b0010, ?G => 0b0100, ?T => 0b1000}
  @code_to_nucleotide %{0b0000 => ?\s, 0b0001 => ?A, 0b0010 => ?C, 0b0100 => ?G, 0b1000 => ?T}

  def encode_nucleotide(code_point) do
    @nucleotide_to_code[code_point]
  end

  def decode_nucleotide(encoded_code) do
    @code_to_nucleotide[encoded_code]
  end

  def encode(dna) do
    do_encode(dna, <<>>)
  end

  defp do_encode([], encoded) do
    encoded
  end

  defp do_encode([cp | rest], encoded) do
    do_encode(
      rest,
      <<encoded::bitstring, encode_nucleotide(cp)::size(4)>>
    )
  end

  def decode(dna) do
    do_decode(dna, '')
  end

  defp do_decode(<<>>, decoded) do
    decoded
  end

  defp do_decode(<<code::4, rest::bitstring>>, decoded) do
    do_decode(
      rest,
      decoded ++ [decode_nucleotide(code)]
    )
  end
end
