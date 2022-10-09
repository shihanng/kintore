local function enc(s, count, char)
	local res = s
	if count > 1 then
		res = res .. count
	end

	return res .. char
end

return {
	encode = function(s)
		if #s == 0 then
			return s
		end

		local encoded = ""
		local curr_char = string.sub(s, 1, 1)
		local curr_count = 1

		for i = 2, #s do
			local char = string.sub(s, i, i)
			if char == curr_char then
				curr_count = curr_count + 1
			else
				encoded = enc(encoded, curr_count, curr_char)
				curr_char = char
				curr_count = 1
			end
		end

		return enc(encoded, curr_count, curr_char)
	end,

	decode = function(s)
		local num = ""
		local decoded = ""

		for i = 1, #s do
			local char = string.sub(s, i, i)

			if tonumber(char, 10) == nil then
				local n = tonumber(num, 10)
				if n == nil then
					decoded = decoded .. char
				else
					decoded = decoded .. string.rep(char, n)
				end
				num = ""
			else
				num = num .. char
			end
		end

		return decoded
	end,
}
