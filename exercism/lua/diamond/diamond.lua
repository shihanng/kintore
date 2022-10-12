local base = string.byte("A") - 1
return function(which)
	local code = string.byte(which) - base
	local first = string.rep(" ", code - 1) .. "A" .. string.rep(" ", code - 1) .. "\n"

	res = first

	top = { first }
	for i = 2, code do
		local outer_space = string.rep(" ", code - i)
		local inner_space = string.rep(" ", i * 2 - 3)
		local char = string.char(i + base)
		local line = outer_space .. char .. inner_space .. char .. outer_space .. "\n"

		table.insert(top, line)
		res = res .. line
	end

	for i = #top - 1, 1, -1 do
		res = res .. top[i]
	end

	return res
end
