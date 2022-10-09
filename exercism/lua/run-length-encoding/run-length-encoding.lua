return {
	encode = function(s)
		for char in s:gmatch(".") do
			s = s:gsub(char:rep(2) .. "+", function(c)
				return #c .. char
			end)
		end
		return s
	end,

	decode = function(s)
		return s:gsub("(%d+)([%a%s])", function(n, w)
			return w:rep(n)
		end)
	end,
}
