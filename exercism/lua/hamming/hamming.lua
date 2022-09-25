local Hamming = {}

function Hamming.compute(a, b)
	local dist = 0

	if #a ~= #b then
		return -1
	end

	for i = 1, #a do
		local char_a = a:sub(i, i)
		local char_b = b:sub(i, i)

		if char_a ~= char_b then
			dist = dist + 1
		end
	end

	return dist
end

return Hamming
