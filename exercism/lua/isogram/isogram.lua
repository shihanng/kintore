return function(s)
	local ls = string.lower(s)
	local founds = {}

	for i = 1, #ls do
		local char = ls:sub(i, i)

		if founds[char] ~= nil then
			return false
		end

		if char ~= " " and char ~= "-" then
			founds[char] = true
		end
	end

	return true
end
