local DNA = { nucleotideCounts = {} }

function DNA:count(n)
	return self.nucleotideCounts[n] or error("Invalid Nucleotide")
end

function DNA:new(s)
	local obj = {}
	obj.nucleotideCounts = { A = 0, T = 0, C = 0, G = 0 }

	s:gsub(".", function(c)
		local cur_val = obj.nucleotideCounts[c] or error("Invalid Sequence")
		obj.nucleotideCounts[c] = cur_val + 1
	end)

	setmetatable(obj, self)
	self.__index = self
	return obj
end

return DNA
