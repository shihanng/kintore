local leap_year = function(number)
	if number % 4 ~= 0 then
		return false
	end

	if number % 100 ~= 0 then
		return true
	end

	return number % 400 == 0
end

return leap_year
