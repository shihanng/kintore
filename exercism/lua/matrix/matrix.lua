return function(s)
	local mat = {}
	for r in s:gmatch("[^\n]+") do
		row = {}
		for c in r:gmatch("[^ ]+") do
			table.insert(row, tonumber(c))
		end

		table.insert(mat, row)
	end

	mat.row = function(n)
		return mat[n]
	end

	mat.column = function(n)
		local col = {}
		for i = 1, #mat do
			table.insert(col, mat[i][n])
		end
		return col
	end

	return mat
end
