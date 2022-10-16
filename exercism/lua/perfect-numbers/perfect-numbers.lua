local function aliquot_sum(n)
	local sum = 0
	local i = 1

	while i <= math.sqrt(n) do
		if n % i == 0 and i ~= n then
			sum = sum + i

			local v = n / i
			if v ~= i and v ~= n then
				sum = sum + v
			end
		end

		i = i + 1
	end

	return sum
end

local function classify(n)
	local sum = aliquot_sum(n)

	if sum == n then
		return "perfect"
	elseif sum > n then
		return "abundant"
	else
		return "deficient"
	end
end

return {
	aliquot_sum = aliquot_sum,
	classify = classify,
}
